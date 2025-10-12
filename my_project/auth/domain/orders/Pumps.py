from __future__ import annotations
from typing import Dict, Any
from my_project import db

class Pump(db.Model):
    __tablename__ = "pumps"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    capacity = db.Column(db.Float)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Pump':
        obj = Pump(
            id=dto_dict.get("id"),
            capacity=dto_dict.get("capacity"),
            location_id=dto_dict.get("location_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "capacity": self.capacity,
            "location_id": self.location_id,
        }
