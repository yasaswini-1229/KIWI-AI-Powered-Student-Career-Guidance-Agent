from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user_schema import UserRegister
from database import get_db
from models.user import User
router = APIRouter()


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }