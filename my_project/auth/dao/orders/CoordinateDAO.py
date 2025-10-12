from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Coordinates import Coordinate

class CoordinateDAO(GeneralDAO):
    _domain_type = Coordinate

    def create(self, coordinate: Coordinate) -> None:
        self._session.add(coordinate)
        self._session.commit()

    def find_all(self) -> List[Coordinate]:
        return self._session.query(Coordinate).all()

    def find_by_id(self, coordinate_id: int) -> Optional[Coordinate]:
        return self._session.query(Coordinate).filter(Coordinate.id == coordinate_id).first()
