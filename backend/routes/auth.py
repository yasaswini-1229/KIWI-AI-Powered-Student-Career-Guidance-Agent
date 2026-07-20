from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from models.user import User

from schemas.user_schema import UserRegister
from schemas.login_schema import UserLogin

from utils.security import hash_password, verify_password
from utils.jwt_handler import (
    create_access_token,
    verify_access_token
)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# ---------------- REGISTER ---------------- #

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully"
    }


# ---------------- LOGIN ---------------- #

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid Email or Password"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid Email or Password"
        )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ---------------- CURRENT USER ---------------- #

@router.get("/me")
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    email = verify_access_token(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }