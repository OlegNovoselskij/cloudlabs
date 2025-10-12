from flask import Flask
from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity.
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each specific entity
    from .orders.CustomersBlueprint import customers_bp
    from .orders.LocationsBlueprint import locations_bp
    from .orders.PumpsBlueprint import pumps_bp
    from .orders.PumpOperationsBlueprint import pump_operations_bp
    from .orders.SensorReadingsBlueprint import sensor_readings_bp
    from .orders.SoplaBlueprint import sopla_bp
    from .orders.SensorsBlueprint import sensors_bp
    from .orders.SensorsCoordinatesBlueprint import sensors_coordinates_bp
    from .orders.SensorsTypeBlueprint import sensors_type_bp
    from .orders.UsersBlueprint import users_bp
    from .orders.CoordinatesBlueprint import coordinates_bp

    # Register each blueprint with the app
    app.register_blueprint(customers_bp)
    app.register_blueprint(locations_bp)
    app.register_blueprint(pumps_bp)
    app.register_blueprint(pump_operations_bp)
    app.register_blueprint(sensor_readings_bp)
    app.register_blueprint(sopla_bp)
    app.register_blueprint(sensors_bp)
    app.register_blueprint(sensors_coordinates_bp)
    app.register_blueprint(sensors_type_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(coordinates_bp)