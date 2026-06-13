from fastapi import FastAPI
from backend.routers import users

app = FastAPI(
    title="NAVIS API"
)

app.include_router(users.router)