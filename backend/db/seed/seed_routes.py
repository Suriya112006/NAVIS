from backend.db.database import SessionLocal
from backend.db.models import Route

db = SessionLocal()

routes = [
    Route(
        route_name="Koyambedu-Airport Metro",
        transport_type="Metro"
    ),
    Route(
        route_name="CMBT-Airport Bus",
        transport_type="Bus"
    )
]

db.add_all(routes)
db.commit()

print("Routes inserted successfully")

db.close()