from fastapi import APIRouter, HTTPException
from datetime import datetime
from models.access_request import AccessRequestCreate, AccessRequestResponse
from database import access_requests_collection, investors_collection
from services.email_service import EmailService
from bson import ObjectId
import secrets

router = APIRouter(prefix="/api/access-requests", tags=["Access Requests"])

def generate_investor_id():
    """Generate unique investor ID (e.g., INV-20231215-ABC123)"""
    date_str = datetime.utcnow().strftime("%Y%m%d")
    random_str = secrets.token_hex(3).upper()
    return f"INV-{date_str}-{random_str}"


@router.post("/", response_model=dict)
def create_access_request(request: AccessRequestCreate):
    """Submit a new access request"""
    
    # Check if email already has a pending request
    existing_request = access_requests_collection.find_one({
        "email": request.email,
        "status": {"$in": ["pending", "approved"]}
    })
    
    if existing_request:
        if existing_request["status"] == "approved":
            raise HTTPException(
                status_code=400,
                detail="You already have an approved access request"
            )
        raise HTTPException(
            status_code=400,
            detail="You already have a pending access request"
        )
    
    # Create request data
    request_data = {
        "email": request.email,
        "full_name": request.full_name, 
        "company": request.company,
        "phone": request.phone,
        "message": request.message,
        "status": "pending",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "admin_notes": None,
        "otp_verified": False,
        "email_verified": False
    }
    
    # Save to database
    result = access_requests_collection.insert_one(request_data)
    
    # Send confirmation email to user
    try:
        EmailService.send_access_request_confirmation(
            request.email,
            request.full_name
        )
    except Exception as e:
        print(f"Failed to send confirmation email: {e}")
    
    # Send notification to admin
    try:
        EmailService.send_admin_notification(request_data)
    except Exception as e:
        print(f"Failed to send admin notification: {e}")
    
    return {
        "message": "Access request submitted successfully",
        "id": str(result.inserted_id),
        "status": "pending",
        "next_step": "Please check your email for OTP verification"
    }


@router.patch("/{request_id}/approve", response_model=dict)
def approve_access_request(request_id: str, admin_notes: str = None):
    """Approve an access request and create investor record"""
    try:
        obj_id = ObjectId(request_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid request ID")
    
    # Get the access request
    request = access_requests_collection.find_one({"_id": obj_id})
    
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    if request["status"] == "approved":
        raise HTTPException(status_code=400, detail="Request already approved")
    
    # Generate unique investor ID
    investor_id = generate_investor_id()
    
    # Check if investor already exists
    existing_investor = investors_collection.find_one({"email": request["email"]})
    
    if existing_investor:
        # Update existing investor
        investors_collection.update_one(
            {"email": request["email"]},
            {
                "$set": {
                    "full_name": request["full_name"],
                    "company": request["company"],
                    "phone": request["phone"],
                    "is_active": True,
                    "updated_at": datetime.utcnow(),
                    "access_request_id": str(request["_id"])
                }
            }
        )
        investor_id = existing_investor["investor_id"]
    else:
        # Create new investor record
        investor_data = {
            "investor_id": investor_id,
            "email": request["email"],
            "full_name": request["full_name"],
            "company": request["company"],
            "phone": request["phone"],
            "access_request_id": str(request["_id"]),
            "is_active": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        investors_collection.insert_one(investor_data)
    
    # Update access request status
    access_requests_collection.update_one(
        {"_id": obj_id},
        {
            "$set": {
                "status": "approved",
                "approved_at": datetime.utcnow(),
                "investor_id": investor_id,
                "admin_notes": admin_notes,
                "updated_at": datetime.utcnow()
            }
        }
    )
    
    # Send approval email to investor
    try:
        EmailService.send_approval_email(
            request["email"],
            request["full_name"],
            investor_id
        )
    except Exception as e:
        print(f"Failed to send approval email: {e}")
    
    return {
        "message": "Access request approved successfully",
        "investor_id": investor_id,
        "email": request["email"],
        "full_name": request["full_name"],
        "approved_at": datetime.utcnow().isoformat()
    }


@router.patch("/{request_id}/deny", response_model=dict)
def deny_access_request(request_id: str, reason: str):
    """Deny an access request"""
    try:
        obj_id = ObjectId(request_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid request ID")
    
    # Get the access request
    request = access_requests_collection.find_one({"_id": obj_id})
    
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    if request["status"] != "pending":
        raise HTTPException(status_code=400, detail="Can only deny pending requests")
    
    # Update access request status
    access_requests_collection.update_one(
        {"_id": obj_id},
        {
            "$set": {
                "status": "denied",
                "denied_at": datetime.utcnow(),
                "denial_reason": reason,
                "updated_at": datetime.utcnow()
            }
        }
    )
    
    # Send denial email to user
    try:
        EmailService.send_denial_email(
            request["email"],
            request["full_name"],
            reason
        )
    except Exception as e:
        print(f"Failed to send denial email: {e}")
    
    return {
        "message": "Access request denied",
        "status": "denied",
        "reason": reason
    }


@router.get("/{request_id}", response_model=dict)
def get_access_request(request_id: str):
    """Get access request status"""
    try:
        request = access_requests_collection.find_one({"_id": ObjectId(request_id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid request ID")
    
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    request["id"] = str(request.pop("_id"))
    request.pop("otp", None)  # Don't expose OTP
    request.pop("otp_expiry", None)
    request.pop("otp_attempts", None)
    
    return request


@router.get("/check/{email}")
def check_access_request_status(email: str):
    """Check if email has an existing access request"""
    request = access_requests_collection.find_one(
        {"email": email},
        sort=[("created_at", -1)]
    )
    
    if not request:
        return {
            "has_request": False,
            "message": "No access request found"
        }
    
    return {
        "has_request": True,
        "status": request["status"],
        "email_verified": request.get("email_verified", False),
        "otp_verified": request.get("otp_verified", False),
        "created_at": request["created_at"],
        "investor_id": request.get("investor_id"),
        "id": str(request["_id"])
    }