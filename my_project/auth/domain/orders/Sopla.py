from __future__ import annotations
from typing import Dict, Any
from my_project import db


class Sopla(db.Model):
    __tablename__ = "sopla"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    max_water_dlow = db.Column(db.Float)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    coordinate_id = db.Column(db.Integer, db.ForeignKey("coordinates.id"), nullable=False)

    @staticmethod
    def create_from_dto(dto_dict: dict) -> 'Sopla':
        obj = Sopla(
            id=dto_dict.get("id"),
            max_water_dlow=dto_dict.get("max_water_dlow"),
            location_id=dto_dict.get("location_id"),
            coordinate_id=dto_dict.get("coordinate_id")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "max_water_dlow": self.max_water_dlow,
            "location_id": self.location_id,
            "coordinate_id": self.coordinate_id,
        }
