from typing import List
from my_project.auth.dao.orders.SensorsCoordinatesDAO import SensorsCoordinatesDAO
from my_project.auth.domain.orders.SensorsCoordinates import SensorsCoordinates

class SensorsCoordinatesController:
    _dao = SensorsCoordinatesDAO()

    @classmethod
    def find_all(cls) -> List[SensorsCoordinates]:
        return cls._dao.find_all()

    def create(self, sensors_coordinates: SensorsCoordinates) -> None:
        self._dao.create(sensors_coordinates)

    def find_by_id(self, sensor_id: int, sensor_type_id: int, coordinate_id: int) -> SensorsCoordinates:
        return self._dao.find_by_id(sensor_id, sensor_type_id, coordinate_id)

    def update(self, sensor_id: int, sensor_type_id: int, coordinate_id: int, sensors_coordinates: SensorsCoordinates) -> None:
        self._dao.update(sensor_id, sensor_type_id, coordinate_id, sensors_coordinates)

    def delete(self, sensor_id: int, sensor_type_id: int, coordinate_id: int) -> None:
        self._dao.delete(sensor_id, sensor_type_id, coordinate_id)
