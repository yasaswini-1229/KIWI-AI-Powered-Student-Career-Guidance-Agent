from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    skills: str
    interest: str
    career_goal: str