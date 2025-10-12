from typing import List, Optional
from my_project.auth.dao.orders.SensorsCoordinatesDAO import SensorsCoordinatesDAO
from my_project.auth.domain.orders.SensorsCoordinates import SensorsCoordinates
from my_project.auth.service.general_service import GeneralService

class SensorsCoordinatesService(GeneralService):
    _dao = SensorsCoordinatesDAO()

    def find_all(self) -> List[SensorsCoordinates]:
        return self._dao.find_all()

    def find_all_expanded(self) -> list:
        return self._dao.find_all_expanded()

    def find_by_id(self, sensor_id: int, coordinate_id: int) -> Optional[SensorsCoordinates]:
        return self._dao.find_by_id(sensor_id, coordinate_id)

    def find_by_sensor_id(self, sensor_id: int) -> List[SensorsCoordinates]:
        return self._dao.find_by_sensor_id(sensor_id)

    def find_by_coordinate_id(self, coordinate_id: int) -> List[SensorsCoordinates]:
        return self._dao.find_by_coordinate_id(coordinate_id)

    def create(self, sensor_coordinate: SensorsCoordinates) -> None:
        self._dao.create(sensor_coordinate)

    def update(self, sensor_coordinate: SensorsCoordinates) -> None:
        self._dao.update(sensor_coordinate)

    def delete(self, sensor_id: int, coordinate_id: int) -> None:
        self._dao.delete(sensor_id, coordinate_id)