from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PumpOperations import PumpOperation

class PumpOperationDAO(GeneralDAO):
    _domain_type = PumpOperation

    def create(self, operation: PumpOperation) -> None:
        self._session.add(operation)
        self._session.commit()

    def find_all(self) -> List[PumpOperation]:
        return self._session.query(PumpOperation).all()

    def find_by_id(self, operation_id: int) -> Optional[PumpOperation]:
        return self._session.query(PumpOperation).filter(PumpOperation.operation_id == operation_id).first()
