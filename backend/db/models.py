from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_type = Column(String, nullable=False)


class Stop(Base):
    __tablename__ = "stops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    stop_type = Column(String)


class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    route_name = Column(String)
    transport_type = Column(String)


class Segment(Base):
    __tablename__ = "segments"

    id = Column(Integer, primary_key=True, index=True)

    route_id = Column(Integer, ForeignKey("routes.id"))

    start_stop_id = Column(Integer, ForeignKey("stops.id"))
    end_stop_id = Column(Integer, ForeignKey("stops.id"))

    fare = Column(Float)
    duration = Column(Float)


class RiskZone(Base):
    __tablename__ = "risk_zones"

    id = Column(Integer, primary_key=True, index=True)
    zone_name = Column(String)
    risk_level = Column(String)
    risk_type = Column(String)