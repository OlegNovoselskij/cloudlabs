from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Pumps import Pump

class PumbDAO(GeneralDAO):
    _domain_type = Pump

    def create(self, pump: Pump) -> None:
        self._session.add(pump)
        self._session.commit()

    def find_all(self) -> List[Pump]:
        return self._session.query(Pump).all()

    def find_by_id(self, pump_id: int) -> Optional[Pump]:
        return self._session.query(Pump).filter(Pump.pump_id == pump_id).first()
