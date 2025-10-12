from __future__ import annotations
from typing import Dict, Any
from my_project import db



class SensorType(db.Model):
    __tablename__ = "sensor_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(45))

    sensors = db.relationship("Sensor", backref="type", lazy=True)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'SensorType':
        obj = SensorType(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            description=dto_dict.get("description")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "sensors": [sensor.id for sensor in self.sensors]
        }
