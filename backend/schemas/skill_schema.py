from pydantic import BaseModel


class SkillCreate(BaseModel):

    student_email: str

    skill: str

    level: str