# Orders DB imports for DAOs corresponding to each entity
from .orders.CoordinateDAO import CoordinateDAO as CoordinatesDAO
from .orders.CustomerDAO import CustomerDAO as CustomersDAO
from .orders.LocationDAO import LocationDAO as LocationsDAO
from .orders.PumpDAO import PumpDAO as PumpsDAO
from .orders.PumpOperationDAO import PumpOperationDAO as PumpOperationsDAO
from .orders.SensorReadingDAO import SensorReadingDAO as SensorReadingsDAO
from .orders.SensorsCoordinatesDAO import SensorsCoordinatesDAO
from .orders.SensorDAO import SensorDAO as SensorsDAO
from .orders.SensorTypeDAO import SensorTypeDAO as SensorsTypeDAO
from .orders.SoplaDAO import SoplaDAO
from .orders.UserDAO import UserDAO

# Initialize DAOs for each entity
coordinates_dao = CoordinatesDAO()
customers_dao = CustomersDAO()
locations_dao = LocationsDAO()
pumps_dao = PumpsDAO()
pump_operations_dao = PumpOperationsDAO()
sensor_readings_dao = SensorReadingsDAO()
sensors_coordinates_dao = SensorsCoordinatesDAO()
sensors_dao = SensorsDAO()
sensors_type_dao = SensorsTypeDAO()
sopla_dao = SoplaDAO()
users_dao = UserDAO()

# Export all DAO instances
__all__ = [
    'coordinates_dao',
    'customers_dao',
    'locations_dao',
    'pumps_dao',
    'pump_operations_dao',
    'sensor_readings_dao',
    'sensors_coordinates_dao',
    'sensors_dao',
    'sensors_type_dao',
    'sopla_dao',
    'users_dao'
]
