from typing import List
from my_project.auth.dao.orders.SoplaDAO import SoplaDAO
from my_project.auth.domain.orders.Sopla import Sopla

class SoplaController:
    _dao = SoplaDAO()

    @classmethod
    def find_all(cls) -> List[Sopla]:
        return cls._dao.find_all()

    def create(self, sopla: Sopla) -> None:
        self._dao.create(sopla)

    def find_by_id(self, sopla_id: int) -> Sopla:
        return self._dao.find_by_id(sopla_id)

    def update(self, sopla_id: int, sopla: Sopla) -> None:
        self._dao.update(sopla_id, sopla)

    def delete(self, sopla_id: int) -> None:
        self._dao.delete(sopla_id)
