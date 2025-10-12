from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Coordinates import Coordinate
from my_project.auth.service.orders.CoordinatesService import CoordinatesService

coordinates_service = CoordinatesService()
coordinates_bp = Blueprint('coordinates', __name__, url_prefix='/coordinates')

@coordinates_bp.get('')
def get_all_coordinates() -> Response:
    coordinates = coordinates_service.find_all()
    coordinates_dto = [coordinate.put_into_dto() for coordinate in coordinates]
    return make_response(jsonify(coordinates_dto), HTTPStatus.OK)

@coordinates_bp.post('')
def create_coordinate() -> Response:
    content = request.get_json()
    coordinate = Coordinate.create_from_dto(content)
    coordinates_service.create(coordinate)
    return make_response(jsonify(coordinate.put_into_dto()), HTTPStatus.CREATED)

@coordinates_bp.get('/<int:coordinate_id>')
def get_coordinate(coordinate_id: int) -> Response:
    coordinate = coordinates_service.find_by_id(coordinate_id)
    if coordinate:
        return make_response(jsonify(coordinate.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Coordinate not found"}), HTTPStatus.NOT_FOUND)

@coordinates_bp.put('/<int:coordinate_id>')
def update_coordinate(coordinate_id: int) -> Response:
    content = request.get_json()
    coordinate = coordinates_service.find_by_id(coordinate_id)
    if not coordinate:
        return make_response(jsonify({"error": "Coordinate not found"}), HTTPStatus.NOT_FOUND)

    updated_coordinate = Coordinate.create_from_dto(content)
    coordinates_service.update(coordinate_id, updated_coordinate)
    return make_response(jsonify(updated_coordinate.put_into_dto()), HTTPStatus.OK)

@coordinates_bp.delete('/<int:coordinate_id>')
def delete_coordinate(coordinate_id: int) -> Response:
    coordinate = coordinates_service.find_by_id(coordinate_id)
    if not coordinate:
        return make_response(jsonify({"error": "Coordinate not found"}), HTTPStatus.NOT_FOUND)

    coordinates_service.delete(coordinate_id)
    return make_response(jsonify({"message": "Coordinate deleted successfully"}), HTTPStatus.NO_CONTENT)
