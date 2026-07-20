from fastapi import FastAPI
from config.settings import APP_NAME, APP_VERSION
from database import Base, engine
from routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": f"Welcome to {APP_NAME}",
        "status": "Running Successfully"
    }