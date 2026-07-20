from fastapi import APIRouter
from schemas.roadmap_schema import RoadmapRequest

router = APIRouter()


@router.post("/roadmap")
def generate_roadmap(data: RoadmapRequest):

    career = data.career.lower()

    roadmap = []

    if career == "ai engineer":

        roadmap = [
            "Learn Python",
            "Learn SQL",
            "Learn Statistics",
            "Learn Machine Learning",
            "Learn Deep Learning",
            "Learn Generative AI",
            "Learn LangChain",
            "Learn LangGraph",
            "Build 5 AI Projects",
            "Create Resume",
            "Prepare for Interviews",
            "Apply for Jobs"
        ]

    elif career == "data scientist":

        roadmap = [
            "Learn Python",
            "Learn SQL",
            "Learn Statistics",
            "Learn Pandas",
            "Learn NumPy",
            "Learn Data Visualization",
            "Learn Machine Learning",
            "Build Data Science Projects",
            "Create Resume",
            "Apply for Jobs"
        ]

    elif career == "python developer":

        roadmap = [
            "Learn Python Basics",
            "Learn OOP",
            "Learn File Handling",
            "Learn APIs",
            "Learn FastAPI",
            "Learn SQL",
            "Learn Git & GitHub",
            "Build Projects",
            "Prepare Resume",
            "Apply for Jobs"
        ]

    else:

        roadmap = [
            "Learn Programming",
            "Build Projects",
            "Practice Daily",
            "Prepare Resume",
            "Apply for Jobs"
        ]

    return {
        "career": data.career,
        "roadmap": roadmap
    }