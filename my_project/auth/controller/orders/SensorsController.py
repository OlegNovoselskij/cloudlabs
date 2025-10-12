from typing import List
from my_project.auth.dao.orders.SensorsDAO import SensorsDAO
from my_project.auth.domain.orders.Sensors import Sensor

class SensorsController:
    _dao = SensorsDAO()

    @classmethod
    def find_all(cls) -> List[Sensor]:
        return cls._dao.find_all()

    def create(self, sensor: Sensor) -> None:
        self._dao.create(sensor)

    def find_by_id(self, sensor_id: int) -> Sensor:
        return self._dao.find_by_id(sensor_id)

    def update(self, sensor_id: int, sensor: Sensor) -> None:
        self._dao.update(sensor_id, sensor)

    def delete(self, sensor_id: int) -> None:
        self._dao.delete(sensor_id)
