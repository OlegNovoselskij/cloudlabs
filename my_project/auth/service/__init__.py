from .orders.CoordinatesService import CoordinatesService
from .orders.CustomersService import CustomersService
from .orders.LocationsService import LocationsService
from .orders.PumpsService import PumpsService
from .orders.PumpOperationsService import PumpOperationsService
from .orders.SensorReadingsService import SensorReadingsService
from .orders.SoplaService import SoplaService
from .orders.SensorsService import SensorsService
from .orders.SensorsCoordinatesService import SensorsCoordinatesService
from .orders.SensorsTypeService import SensorsTypeService
from .orders.UsersService import UsersService

# Initialize all services
coordinatesService = CoordinatesService()
customersService = CustomersService()
locationsService = LocationsService()
pumpsService = PumpsService()
pumpOperationsService = PumpOperationsService()
sensorReadingsService = SensorReadingsService()
soplaService = SoplaService()
sensorsService = SensorsService()
sensorsCoordinatesService = SensorsCoordinatesService()
sensorsTypeService = SensorsTypeService()
usersService = UsersService()

# Export all service instances
__all__ = [
    'coordinatesService',
    'customersService',
    'locationsService',
    'pumpsService',
    'pumpOperationsService',
    'sensorReadingsService',
    'soplaService',
    'sensorsService',
    'sensorsCoordinatesService',
    'sensorsTypeService',
    'usersService'
]

