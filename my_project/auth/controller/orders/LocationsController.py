from typing import List
from my_project.auth.dao.orders.LocationsDAO import LocationsDAO
from my_project.auth.domain.orders.Locations import Location

class LocationsController:
    _dao = LocationsDAO()

    @classmethod
    def find_all(cls) -> List[Location]:
        return cls._dao.find_all()

    def create(self, location: Location) -> None:
        self._dao.create(location)

    def find_by_id(self, location_id: int) -> Location:
        return self._dao.find_by_id(location_id)

    def update(self, location_id: int, location: Location) -> None:
        self._dao.update(location_id, location)

    def delete(self, location_id: int) -> None:
        self._dao.delete(location_id)
