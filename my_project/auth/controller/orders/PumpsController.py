from typing import List
from my_project.auth.dao.orders.PumpsDAO import PumpsDAO
from my_project.auth.domain.orders.Pumps import Pumps

class PumpsController:
    _dao = PumpsDAO()

    @classmethod
    def find_all(cls) -> List[Pumps]:
        return cls._dao.find_all()

    def create(self, pump: Pumps) -> None:
        self._dao.create(pump)

    def find_by_id(self, pump_id: int) -> Pumps:
        return self._dao.find_by_id(pump_id)

    def update(self, pump_id: int, pump: Pumps) -> None:
        self._dao.update(pump_id, pump)

    def delete(self, pump_id: int) -> None:
        self._dao.delete(pump_id)
