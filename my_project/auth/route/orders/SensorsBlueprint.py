from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Sensors import Sensor
from my_project.auth.service.orders.SensorsService import SensorsService
from my_project.auth.service.orders.SensorsCoordinatesService import SensorsCoordinatesService

sensors_service = SensorsService()
sensorscoordinates_service = SensorsCoordinatesService()
sensors_bp = Blueprint('sensors', __name__, url_prefix='/sensors')

@sensors_bp.get('')
def get_all_sensors() -> Response:
    sensors = sensors_service.find_all()
    sensors_dto = [sensor.put_into_dto() for sensor in sensors]
    return make_response(jsonify(sensors_dto), HTTPStatus.OK)

@sensors_bp.post('')
def create_sensor() -> Response:
    content = request.get_json()
    sensor = Sensor.create_from_dto(content)
    sensors_service.create(sensor)
    return make_response(jsonify(sensor.put_into_dto()), HTTPStatus.CREATED)

@sensors_bp.get('/<int:sensor_id>')
def get_sensor(sensor_id: int) -> Response:
    sensor = sensors_service.find_by_id(sensor_id)
    if sensor:
        return make_response(jsonify(sensor.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Sensor not found"}), HTTPStatus.NOT_FOUND)

@sensors_bp.put('/<int:sensor_id>')
def update_sensor(sensor_id: int) -> Response:
    content = request.get_json()
    sensor = sensors_service.find_by_id(sensor_id)
    if not sensor:
        return make_response(jsonify({"error": "Sensor not found"}), HTTPStatus.NOT_FOUND)

    updated_sensor = Sensor.create_from_dto(content)
    updated_sensor.sensor_id = sensor_id
    sensors_service.update(updated_sensor)
    return make_response(jsonify(updated_sensor.put_into_dto()), HTTPStatus.OK)

@sensors_bp.delete('/<int:sensor_id>')
def delete_sensor(sensor_id: int) -> Response:
    sensor = sensors_service.find_by_id(sensor_id)
    if not sensor:
        return make_response(jsonify({"error": "Sensor not found"}), HTTPStatus.NOT_FOUND)

    sensors_service.delete(sensor_id)
    return make_response(jsonify({"message": "Sensor deleted successfully"}), HTTPStatus.NO_CONTENT)

@sensors_bp.get('/<int:sensor_id>/sensorreadings')
def get_sensorreadings_by_sensor(sensor_id: int) -> Response:
    from my_project.auth.service.orders.SensorReadingsService import SensorReadingsService
    sensorreadings_service = SensorReadingsService()
    sensorreadings = sensorreadings_service.get_by_sensor_id(sensor_id)
    sensorreadings_dto = [sr.put_into_dto() for sr in sensorreadings]
    return make_response(jsonify(sensorreadings_dto), HTTPStatus.OK)

@sensors_bp.get('/<int:sensor_id>/coordinates')
def get_coordinates_by_sensor(sensor_id: int) -> Response:
    sensorscoordinates = sensorscoordinates_service.find_by_sensor_id(sensor_id)
    sensorscoordinates_dto = [sc.put_into_dto() for sc in sensorscoordinates]
    return make_response(jsonify(sensorscoordinates_dto), HTTPStatus.OK)
