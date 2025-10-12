from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Sensors import Sensor

class SensorDAO(GeneralDAO):
    _domain_type = Sensor

    def create(self, sensor: Sensor) -> None:
        self._session.add(sensor)
        self._session.commit()

    def find_all(self) -> List[Sensor]:
        return self._session.query(Sensor).all()

    def find_by_id(self, sensor_id: int) -> Sensor:
        return self._session.query(Sensor).filter(Sensor.id == sensor_id).first()

    def find_by_type_id(self, type_id: int) -> List[Sensor]:
        return self._session.query(Sensor).filter(Sensor.sensor_type_id == type_id).all()
