from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.SensorReadings import SensorReading

class SensorReadingDAO(GeneralDAO):
    _domain_type = SensorReading

    def create(self, reading: SensorReading) -> None:
        self._session.add(reading)
        self._session.commit()

    def find_all(self) -> List[SensorReading]:
        return self._session.query(SensorReading).all()

    def find_by_id(self, reading_id: int) -> Optional[SensorReading]:
        return self._session.query(SensorReading).filter(SensorReading.sensor_reading_id == reading_id).first()

    def find_by_sensor_id(self, sensor_id: int) -> List[SensorReading]:
        return self._session.query(SensorReading).filter(SensorReading.sensor_id == sensor_id).all()
