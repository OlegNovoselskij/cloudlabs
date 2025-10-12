from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.SensorReadings import SensorReading
from my_project.auth.service.orders.SensorReadingsService import SensorReadingsService

sensorreadings_service = SensorReadingsService()
sensor_readings_bp = Blueprint('sensorreadings', __name__, url_prefix='/sensorreadings')

@sensor_readings_bp.get('')
def get_all_sensorreadings() -> Response:
    sensorreadings = sensorreadings_service.find_all()
    sensorreadings_dto = [sr.put_into_dto() for sr in sensorreadings]
    return make_response(jsonify(sensorreadings_dto), HTTPStatus.OK)

@sensor_readings_bp.post('')
def create_sensorreading() -> Response:
    content = request.get_json()
    sensorreading = SensorReading.create_from_dto(content)
    sensorreadings_service.create(sensorreading)
    return make_response(jsonify(sensorreading.put_into_dto()), HTTPStatus.CREATED)

@sensor_readings_bp.get('/<int:sensor_reading_id>')
def get_sensorreading(sensor_reading_id: int) -> Response:
    sensorreading = sensorreadings_service.find_by_id(sensor_reading_id)
    if sensorreading:
        return make_response(jsonify(sensorreading.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "SensorReading not found"}), HTTPStatus.NOT_FOUND)

@sensor_readings_bp.put('/<int:sensor_reading_id>')
def update_sensorreading(sensor_reading_id: int) -> Response:
    content = request.get_json()
    sensorreading = sensorreadings_service.find_by_id(sensor_reading_id)
    if not sensorreading:
        return make_response(jsonify({"error": "SensorReading not found"}), HTTPStatus.NOT_FOUND)

    updated_sensorreading = SensorReading.create_from_dto(content)
    updated_sensorreading.sensor_reading_id = sensor_reading_id
    sensorreadings_service.update(updated_sensorreading)
    return make_response(jsonify(updated_sensorreading.put_into_dto()), HTTPStatus.OK)

@sensor_readings_bp.delete('/<int:sensor_reading_id>')
def delete_sensorreading(sensor_reading_id: int) -> Response:
    sensorreading = sensorreadings_service.find_by_id(sensor_reading_id)
    if not sensorreading:
        return make_response(jsonify({"error": "SensorReading not found"}), HTTPStatus.NOT_FOUND)

    sensorreadings_service.delete(sensor_reading_id)
    return make_response(jsonify({"message": "SensorReading deleted successfully"}), HTTPStatus.NO_CONTENT)
