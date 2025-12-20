from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from bson import ObjectId
from models.qa import QuestionCreate, AnswerCreate, QAThreadResponse
from routers.admin_auth import require_admin
from services.qa import QAService
from services.auth_service import AuthService
from database import admin_users_collection, investors_collection

router = APIRouter(prefix="/api/qa", tags=["Q&A"])
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


@router.post("/questions", response_model=dict)
def submit_question(
    question: QuestionCreate,
    current_user: dict = Depends(get_current_user_or_investor)
):
    """Submit a new question"""
    question_id = QAService.submit_question(
        user_id=current_user["id"],
        question_text=question.question_text,
        category=question.category,
        is_urgent=question.is_urgent
    )
    return {"message": "Question submitted successfully", "id": question_id}

@router.get("/threads", response_model=List[QAThreadResponse])
def get_qa_threads(
    current_user: dict = Depends(get_current_user_or_investor)
):
    """Get Q&A threads for current user"""
    threads = QAService.get_qa_threads(current_user["id"])
    return threads

@router.get("/search")
def search_qa(
    q: str = Query(..., min_length=3),
    current_user: dict = Depends(get_current_user_or_investor)
):
    """Search public Q&A threads"""
    results = QAService.search_qa(q)
    return results

@router.post("/questions/{question_id}/answer")
def answer_question(
    question_id: str,
    answer: AnswerCreate,
    current_admin: dict = Depends(require_admin)
):
    """Answer a question (Admin only)"""
    success = QAService.answer_question(
        question_id=question_id,
        admin_id=current_admin["id"],
        answer_text=answer.answer_text,
        is_public=answer.is_public
    )
    
    if success:
        return {"message": "Answer posted successfully"}
    raise HTTPException(status_code=400, detail="Failed to post answer")
