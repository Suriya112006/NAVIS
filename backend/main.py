from fastapi import FastAPI
from backend.routers import users
from backend.routers import fare
from backend.routers import risk
from backend.routers import crowd
from backend.routers import stop
from backend.routers import routes
from backend.routers import journey

app = FastAPI(
    title="NAVIS API"
)

app.include_router(users.router)
app.include_router(fare.router)
app.include_router(risk.router)
app.include_router(crowd.router)
app.include_router(stop.router)
app.include_router(routes.router)
app.include_router(journey.router)