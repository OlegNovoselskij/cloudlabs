from __future__ import annotations
from typing import Dict, Any
from my_project import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    phone = db.Column(db.String(45))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "location_id": self.location_id,
        }
