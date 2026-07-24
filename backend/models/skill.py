from sqlalchemy import Column, Integer, String
from database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    student_email = Column(
        String,
        nullable=False
    )

    skill = Column(
        String,
        nullable=False
    )

    level = Column(
        String,
        nullable=False
    )