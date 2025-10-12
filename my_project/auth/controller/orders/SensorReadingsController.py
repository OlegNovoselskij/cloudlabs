from typing import List
from my_project.auth.dao.orders.SensorReadingsDAO import SensorReadingsDAO
from my_project.auth.domain.orders.SensorReadings import SensorReadings

class SensorReadingsController:
    _dao = SensorReadingsDAO()

    @classmethod
    def find_all(cls) -> List[SensorReadings]:
        return cls._dao.find_all()

    def create(self, sensor_reading: SensorReadings) -> None:
        self._dao.create(sensor_reading)

    def find_by_id(self, sensor_reading_id: int) -> SensorReadings:
        return self._dao.find_by_id(sensor_reading_id)

    def update(self, sensor_reading_id: int, sensor_reading: SensorReadings) -> None:
        self._dao.update(sensor_reading_id, sensor_reading)

    def delete(self, sensor_reading_id: int) -> None:
        self._dao.delete(sensor_reading_id)
