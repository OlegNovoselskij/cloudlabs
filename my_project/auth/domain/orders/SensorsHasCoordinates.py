from __future__ import annotations
from typing import Dict, Any
from my_project import db


class SensorCoordinate(db.Model):
    __tablename__ = "sensors_has_coordinates"

    sensors_sensor_id = db.Column(db.Integer, primary_key=True)
    sensors_FK_sensor_type_id = db.Column(db.Integer, primary_key=True)
    coordinates_coordinate_id = db.Column(db.Integer, db.ForeignKey("coordinates.coordinate_id"), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "sensors_sensor_id": self.sensors_sensor_id,
            "sensors_FK_sensor_type_id": self.sensors_FK_sensor_type_id,
            "coordinates_coordinate_id": self.coordinates_coordinate_id,
        }
