from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.SensorsCoordinates import SensorsCoordinates
from my_project.auth.service.orders.SensorsCoordinatesService import SensorsCoordinatesService

sensorscoordinates_service = SensorsCoordinatesService()
sensors_coordinates_bp = Blueprint('sensorscoordinates', __name__, url_prefix='/sensorscoordinates')

@sensors_coordinates_bp.get('')
def get_all_sensorscoordinates() -> Response:
    data = sensorscoordinates_service.find_all_expanded()
    return make_response(jsonify(data), HTTPStatus.OK)

@sensors_coordinates_bp.get('/expanded')
def get_all_sensorscoordinates_expanded() -> Response:
    data = sensorscoordinates_service.find_all_expanded()
    return make_response(jsonify(data), HTTPStatus.OK)

@sensors_coordinates_bp.post('')
def create_sensorscoordinates() -> Response:
    content = request.get_json()
    sensorscoordinates = SensorsCoordinates.create_from_dto(content)
    sensorscoordinates_service.create(sensorscoordinates)
    return make_response(jsonify(sensorscoordinates.put_into_dto()), HTTPStatus.CREATED)

@sensors_coordinates_bp.get('/<int:sensor_id>/<int:coordinate_id>')
def get_sensorscoordinates(sensor_id: int, coordinate_id: int) -> Response:
    sensorscoordinates = sensorscoordinates_service.find_by_id(sensor_id, coordinate_id)
    if sensorscoordinates:
        return make_response(jsonify(sensorscoordinates.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "SensorsCoordinates not found"}), HTTPStatus.NOT_FOUND)

@sensors_coordinates_bp.put('/<int:sensor_id>/<int:coordinate_id>')
def update_sensorscoordinates(sensor_id: int, coordinate_id: int) -> Response:
    content = request.get_json()
    sensorscoordinates = sensorscoordinates_service.find_by_id(sensor_id, coordinate_id)
    if not sensorscoordinates:
        return make_response(jsonify({"error": "SensorsCoordinates not found"}), HTTPStatus.NOT_FOUND)

    updated_sensorscoordinates = SensorsCoordinates.create_from_dto(content)
    sensorscoordinates_service.update(updated_sensorscoordinates)
    return make_response(jsonify(updated_sensorscoordinates.put_into_dto()), HTTPStatus.OK)

@sensors_coordinates_bp.delete('/<int:sensor_id>/<int:coordinate_id>')
def delete_sensorscoordinates(sensor_id: int, coordinate_id: int) -> Response:
    sensorscoordinates = sensorscoordinates_service.find_by_id(sensor_id, coordinate_id)
    if not sensorscoordinates:
        return make_response(jsonify({"error": "SensorsCoordinates not found"}), HTTPStatus.NOT_FOUND)

    sensorscoordinates_service.delete(sensor_id, coordinate_id)
    return make_response(jsonify({"message": "SensorsCoordinates deleted successfully"}), HTTPStatus.NO_CONTENT)
