from __future__ import annotations
from typing import Dict, Any
from my_project import db
from datetime import datetime


class SensorReading(db.Model):
    __tablename__ = "sensor_readings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float)
    unit = db.Column(db.String(10))
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"), nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'SensorReading':
        obj = SensorReading(
            id=dto_dict.get("id"),
            timestamp=datetime.fromisoformat(dto_dict.get("timestamp")) if dto_dict.get("timestamp") else None,
            value=dto_dict.get("value"),
            unit=dto_dict.get("unit"),
            sensor_id=dto_dict.get("sensor_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "value": self.value,
            "unit": self.unit,
            "sensor_id": self.sensor_id,
        }
