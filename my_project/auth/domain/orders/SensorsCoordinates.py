from __future__ import annotations
from typing import Dict, Any
from my_project import db

class SensorsCoordinates(db.Model):
    __tablename__ = "sensors_coordinates"

    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"), primary_key=True)
    coordinate_id = db.Column(db.Integer, db.ForeignKey("coordinates.id"), primary_key=True)

    sensor = db.relationship("Sensor", backref=db.backref("sensors_coordinates_assoc", cascade="all, delete-orphan"))
    coordinate = db.relationship("Coordinate", backref=db.backref("sensors_coordinates_assoc", cascade="all, delete-orphan"))

    def __init__(self, sensor_id: int, coordinate_id: int):
        self.sensor_id = sensor_id
        self.coordinate_id = coordinate_id

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sensor_id": self.sensor_id,
            "coordinate_id": self.coordinate_id
        }

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'SensorsCoordinates':
        return SensorsCoordinates(
            sensor_id=dto_dict.get("sensor_id"),
            coordinate_id=dto_dict.get("coordinate_id")
        ) 