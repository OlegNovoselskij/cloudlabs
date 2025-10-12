from typing import List
from my_project.auth.dao.orders.PumpOperationsDAO import PumpOperationsDAO
from my_project.auth.domain.orders.PumpOperations import PumpOperations

class PumpOperationsController:
    _dao = PumpOperationsDAO()

    @classmethod
    def find_all(cls) -> List[PumpOperations]:
        return cls._dao.find_all()

    def create(self, pump_operation: PumpOperations) -> None:
        self._dao.create(pump_operation)

    def find_by_id(self, pump_operation_id: int) -> PumpOperations:
        return self._dao.find_by_id(pump_operation_id)

    def update(self, pump_operation_id: int, pump_operation: PumpOperations) -> None:
        self._dao.update(pump_operation_id, pump_operation)

    def delete(self, pump_operation_id: int) -> None:
        self._dao.delete(pump_operation_id)
