from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from bson import ObjectId
from services.company_info_service import CompanyInfoService
from services.auth_service import AuthService
from database import admin_users_collection, investors_collection

router = APIRouter(prefix="/api/company", tags=["Company Information"])
security = HTTPBearer()


def get_current_user_or_investor(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user from token - supports both admin and investor tokens"""
    token = credentials.credentials
    payload = AuthService.verify_token(token)
    
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user_id = payload["sub"]
    
    # Check if it's an investor token first
    if payload.get("is_investor"):
        investor = investors_collection.find_one({"_id": ObjectId(user_id)})
        if investor:
            return {
                "id": str(investor["_id"]),
                "email": investor.get("email", ""),
                "full_name": investor.get("full_name", ""),
                "role": "investor",
                "is_admin": False
            }
    
    # Then check admin users
    admin_user = admin_users_collection.find_one({"_id": ObjectId(user_id)})
    if admin_user:
        return {
            "id": str(admin_user["_id"]),
            "email": admin_user.get("email", ""),
            "full_name": admin_user.get("full_name", ""),
            "role": admin_user.get("role", "admin"),
            "is_admin": True
        }
    
    # Finally check investors collection without the token flag
    investor = investors_collection.find_one({"_id": ObjectId(user_id)})
    if investor:
        return {
            "id": str(investor["_id"]),
            "email": investor.get("email", ""),
            "full_name": investor.get("full_name", ""),
            "role": "investor",
            "is_admin": False
        }
    
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/executive-summary")
def get_executive_summary(current_user: dict = Depends(get_current_user_or_investor)):
    """Get executive summary with key highlights"""
    return CompanyInfoService.get_executive_summary()

@router.get("/metrics")
def get_key_metrics(current_user: dict = Depends(get_current_user_or_investor)):
    """Get key company metrics"""
    return CompanyInfoService.get_key_metrics()

@router.get("/milestones")
def get_milestones(current_user: dict = Depends(get_current_user_or_investor)):
    """Get company milestones"""
    return CompanyInfoService.get_milestones()

@router.get("/testimonials")
def get_testimonials(
    featured_only: bool = False,
    current_user: dict = Depends(get_current_user_or_investor)
):
    """Get customer testimonials"""
    return CompanyInfoService.get_testimonials(featured_only)

@router.get("/awards")
def get_awards(current_user: dict = Depends(get_current_user_or_investor)):
    """Get company awards"""
    return CompanyInfoService.get_awards()

@router.get("/media-coverage")
def get_media_coverage(current_user: dict = Depends(get_current_user_or_investor)):
    """Get media coverage"""
    return CompanyInfoService.get_media_coverage()