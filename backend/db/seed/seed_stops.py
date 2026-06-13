from backend.db.database import SessionLocal
from backend.db.models import Stop

db = SessionLocal()

stops = [
    Stop(name="Koyambedu", latitude=13.069, longitude=80.194, stop_type="Metro"),
    Stop(name="CMBT", latitude=13.068, longitude=80.205, stop_type="Bus"),
    Stop(name="Vadapalani", latitude=13.050, longitude=80.212, stop_type="Metro"),
    Stop(name="Guindy", latitude=13.006, longitude=80.220, stop_type="Metro"),
    Stop(name="Airport", latitude=12.981, longitude=80.163, stop_type="Metro"),
]

db.add_all(stops)
db.commit()

print("Stops inserted successfully")

db.close()