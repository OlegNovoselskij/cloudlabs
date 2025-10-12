from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Coordinate(db.Model):
    __tablename__ = "coordinates"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    sensors = db.relationship(
        "Sensor",
        secondary="sensors_coordinates",
        back_populates="coordinates"
    )

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Coordinate':
        obj = Coordinate(
            id=dto_dict.get("id"),
            latitude=dto_dict.get("latitude"),
            longitude=dto_dict.get("longitude")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "sensors": [sensor.id for sensor in self.sensors]
        }
