from fastapi import APIRouter
from schemas.roadmap_schema import RoadmapRequest

router = APIRouter()


@router.post("/roadmap/generate")
def generate_roadmap(data: RoadmapRequest):

    career = data.career.lower()

    if "ai engineer" in career:

        roadmap = [
            "Learn Python Basics",
            "Learn SQL",
            "Learn Statistics",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Learn NLP and Generative AI",
            "Build AI Projects",
            "Learn LangGraph and AI Agents",
            "Prepare Resume and Interviews"
        ]

    elif "data scientist" in career:

        roadmap = [
            "Python",
            "Statistics",
            "Data Analysis",
            "Machine Learning",
            "Data Visualization",
            "Build Data Projects"
        ]

    elif "backend developer" in career:

        roadmap = [
            "Python",
            "FastAPI",
            "Database",
            "REST APIs",
            "Authentication",
            "Deployment"
        ]

    else:

        roadmap = [
            "Learn Programming Basics",
            "Learn Data Structures",
            "Build Projects",
            "Practice Coding"
        ]

    return {
        "career": data.career,
        "roadmap": roadmap
    }