from my_project.auth.controller.orders.CoordinatesController import CoordinatesController
from my_project.auth.controller.orders.CustomersController import CustomersController
from my_project.auth.controller.orders.LocationsController import LocationsController
from my_project.auth.controller.orders.PumpsController import PumpsController
from my_project.auth.controller.orders.PumpOperationsController import PumpOperationsController
from my_project.auth.controller.orders.SensorReadingsController import SensorReadingsController
from my_project.auth.controller.orders.SoplaController import SoplaController
from my_project.auth.controller.orders.SensorsController import SensorsController
from my_project.auth.controller.orders.SensorsCoordinatesController import SensorsCoordinatesController
from my_project.auth.controller.orders.SensorsTypeController import SensorsTypeController



# Initialize controllers
coordinates_controller = CoordinatesController()
customers_controller = CustomersController()
locations_controller = LocationsController()
pumps_controller = PumpsController()
pump_operations_controller = PumpOperationsController()
sensor_readings_controller = SensorReadingsController()
sopla_controller = SoplaController()
sensors_controller = SensorsController()
sensors_coordinates_controller = SensorsCoordinatesController()
sensors_type_controller = SensorsTypeController()