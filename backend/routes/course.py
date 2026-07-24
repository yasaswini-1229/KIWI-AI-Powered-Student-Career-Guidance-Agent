from fastapi import APIRouter
from schemas.course_schema import CourseRequest

router = APIRouter()


@router.post("/courses/recommend")
def recommend_courses(data: CourseRequest):

    topic = data.topic.lower()

    if "python" in topic:
        courses = [
            "Python Basics",
            "Object Oriented Programming",
            "Python Projects",
            "FastAPI Development"
        ]

    elif "sql" in topic:
        courses = [
            "SQL Basics",
            "Joins",
            "Stored Procedures",
            "Database Projects"
        ]

    elif "machine learning" in topic:
        courses = [
            "Linear Regression",
            "Classification",
            "Clustering",
            "ML Projects"
        ]

    elif "langgraph" in topic:
        courses = [
            "LangGraph Basics",
            "State Graph",
            "AI Agents",
            "Multi Agent Systems"
        ]

    else:
        courses = [
            "Introduction Course",
            "Beginner Course",
            "Intermediate Course"
        ]

    return {
        "topic": data.topic,
        "recommended_courses": courses
    }