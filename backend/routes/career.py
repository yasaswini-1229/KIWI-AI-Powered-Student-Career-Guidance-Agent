from fastapi import APIRouter
from schemas.career_schema import CareerRequest

router = APIRouter()


@router.post("/career/recommend")
def recommend_career(data: CareerRequest):

    skills = data.skills.lower()
    interest = data.interest.lower()

    recommendations = []

    if "python" in skills and "artificial intelligence" in interest:
        recommendations = [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist"
        ]

    elif "python" in skills:
        recommendations = [
            "Python Developer",
            "Backend Developer",
            "Automation Engineer"
        ]

    elif "java" in skills:
        recommendations = [
            "Java Developer",
            "Spring Boot Developer",
            "Backend Engineer"
        ]

    elif "sql" in skills:
        recommendations = [
            "Database Administrator",
            "Data Analyst",
            "Business Intelligence Developer"
        ]

    else:
        recommendations = [
            "Software Developer",
            "Full Stack Developer",
            "Cloud Engineer"
        ]

    return {
        "skills": data.skills,
        "interest": data.interest,
        "recommended_careers": recommendations
    }