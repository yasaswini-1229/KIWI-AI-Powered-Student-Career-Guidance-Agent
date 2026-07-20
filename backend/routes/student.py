from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.student import Student
from schemas.student_schema import StudentCreate

router = APIRouter()


# ---------------- CREATE STUDENT PROFILE ---------------- #

@router.post("/student/profile")
def create_student_profile(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    existing_student = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student Profile Already Exists"
        )

    new_student = Student(
        name=student.name,
        email=student.email,
        skills=student.skills,
        interest=student.interest,
        career_goal=student.career_goal
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student Profile Created Successfully"
    }


# ---------------- GET STUDENT PROFILE ---------------- #

@router.get("/student/profile")
def get_student_profile(
    email: str,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.email == email
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Profile Not Found"
        )

    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "skills": student.skills,
        "interest": student.interest,
        "career_goal": student.career_goal
    }
# ---------------- UPDATE STUDENT PROFILE ---------------- #

@router.put("/student/profile")
def update_student_profile(
    email: str,
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    existing_student = db.query(Student).filter(
        Student.email == email
    ).first()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Profile Not Found"
        )

    existing_student.name = student.name
    existing_student.email = student.email
    existing_student.skills = student.skills
    existing_student.interest = student.interest
    existing_student.career_goal = student.career_goal

    db.commit()
    db.refresh(existing_student)

    return {
        "message": "Student Profile Updated Successfully"
    }
# ---------------- DELETE STUDENT PROFILE ---------------- #

@router.delete("/student/profile")
def delete_student_profile(
    email: str,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.email == email
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Profile Not Found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student Profile Deleted Successfully"
    }