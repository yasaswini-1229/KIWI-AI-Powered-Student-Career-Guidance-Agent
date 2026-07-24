from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.skill import Skill
from schemas.skill_schema import SkillCreate


router = APIRouter()


# ---------------- ADD SKILL ---------------- #

@router.post("/skills")
def add_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db)
):

    new_skill = Skill(
        student_email=skill.student_email,
        skill=skill.skill,
        level=skill.level
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return {
        "message": "Skill Added Successfully"
    }


# ---------------- GET STUDENT SKILLS ---------------- #

@router.get("/skills")
def get_skills(
    student_email: str,
    db: Session = Depends(get_db)
):

    skills = db.query(Skill).filter(
        Skill.student_email == student_email
    ).all()

    if not skills:
        raise HTTPException(
            status_code=404,
            detail="No Skills Found"
        )

    return [
        {
            "skill": item.skill,
            "level": item.level
        }
        for item in skills
    ]