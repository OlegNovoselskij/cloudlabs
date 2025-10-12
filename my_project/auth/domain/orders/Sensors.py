from __future__ import annotations
from typing import Dict, Any
from my_project import db
from datetime import datetime



class Sensor(db.Model):
    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    installation_date = db.Column(db.Date)
    type_id = db.Column(db.Integer, db.ForeignKey("sensor_types.id"), nullable=False)

    readings = db.relationship("SensorReading", backref="sensor", lazy=True)
    coordinates = db.relationship(
        "Coordinate",
        secondary="sensors_coordinates",
        back_populates="sensors"
    )

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Sensor':
        obj = Sensor(
            id=dto_dict.get("id"),
            installation_date=datetime.strptime(dto_dict.get("installation_date"), "%Y-%m-%d").date() if dto_dict.get("installation_date") else None,
            type_id=dto_dict.get("type_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "installation_date": str(self.installation_date),
            "type_id": self.type_id,
            "coordinates": [coord.id for coord in self.coordinates]
        }
