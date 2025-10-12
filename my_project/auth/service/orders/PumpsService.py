from typing import List
from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import (
    coordinates_dao, customers_dao, locations_dao, pumps_dao,
    pump_operations_dao, sensor_readings_dao, sensors_coordinates_dao,
    sensors_dao, sensors_type_dao, sopla_dao
)
from my_project.auth.domain.orders.Coordinates import Coordinate
from my_project.auth.domain.orders.Customers import Customer
from my_project.auth.domain.orders.Locations import Location
from my_project.auth.domain.orders.Pumps import Pump
from my_project.auth.domain.orders.PumpOperations import PumpOperation
from my_project.auth.domain.orders.SensorReadings import SensorReading
from my_project.auth.domain.orders.SensorsCoordinates import SensorsCoordinates
from my_project.auth.domain.orders.Sensors import Sensor
from my_project.auth.domain.orders.SensorsType import SensorType
from my_project.auth.domain.orders.Sopla import Sopla


class PumpsService(GeneralService):
    _dao = pumps_dao

    def create(self, item: Pump) -> None:
        self._dao.create(item)

    def get_all(self) -> List[Pump]:
        return self._dao.find_all()

    def get_by_id(self, item_id: int) -> Pump:
        return self._dao.find_by_id(item_id)

    def update(self, item_id: int, item: Pump) -> None:
        self._dao.update(item_id, item)

    def delete(self, item_id: int) -> None:
        self._dao.delete(item_id)