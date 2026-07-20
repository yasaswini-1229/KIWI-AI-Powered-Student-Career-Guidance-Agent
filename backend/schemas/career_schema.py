from pydantic import BaseModel


class CareerRequest(BaseModel):
    skills: str
    interest: str