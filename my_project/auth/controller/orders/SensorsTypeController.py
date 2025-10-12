from typing import List
from my_project.auth.dao.orders.SensorsTypeDAO import SensorsTypeDAO
from my_project.auth.domain.orders.SensorsType import SensorsType

class SensorsTypeController:
    _dao = SensorsTypeDAO()

    @classmethod
    def find_all(cls) -> List[SensorsType]:
        return cls._dao.find_all()

    def create(self, sensor_type: SensorsType) -> None:
        self._dao.create(sensor_type)

    def find_by_id(self, sensor_type_id: int) -> SensorsType:
        return self._dao.find_by_id(sensor_type_id)

    def update(self, sensor_type_id: int, sensor_type: SensorsType) -> None:
        self._dao.update(sensor_type_id, sensor_type)

    def delete(self, sensor_type_id: int) -> None:
        self._dao.delete(sensor_type_id)
