from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Sopla import Sopla

class SoplaDAO(GeneralDAO):
    _domain_type = Sopla

    def create(self, sopla: Sopla) -> None:
        self._session.add(sopla)
        self._session.commit()

    def find_all(self) -> List[Sopla]:
        return self._session.query(Sopla).all()

    def find_by_id(self, sopla_id: int) -> Optional[Sopla]:
        return self._session.query(Sopla).filter(Sopla.id == sopla_id).first()
