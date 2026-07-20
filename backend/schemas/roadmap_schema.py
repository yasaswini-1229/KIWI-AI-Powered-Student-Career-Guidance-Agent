from pydantic import BaseModel


class RoadmapRequest(BaseModel):
    career: str