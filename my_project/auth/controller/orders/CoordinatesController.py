from typing import List
from my_project.auth.dao.orders.CoordinatesDAO import CoordinatesDAO
from my_project.auth.domain.orders.Coordinates import Coordinate

class CoordinatesController:
    _dao = CoordinatesDAO()

    @classmethod
    def find_all(cls) -> List[Coordinate]:
        return cls._dao.find_all()

    def create(self, coordinate: Coordinate) -> None:
        self._dao.create(coordinate)

    def find_by_id(self, coordinate_id: int) -> Coordinate:
        return self._dao.find_by_id(coordinate_id)

    def update(self, coordinate_id: int, coordinate: Coordinate) -> None:
        self._dao.update(coordinate_id, coordinate)

    def delete(self, coordinate_id: int) -> None:
        self._dao.delete(coordinate_id)
