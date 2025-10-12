from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Locations import Location
from my_project.auth.service.orders.LocationsService import LocationsService

locations_service = LocationsService()
locations_bp = Blueprint('locations', __name__, url_prefix='/locations')

@locations_bp.get('')
def get_all_locations() -> Response:
    locations = locations_service.find_all()
    locations_dto = [location.put_into_dto() for location in locations]
    return make_response(jsonify(locations_dto), HTTPStatus.OK)

@locations_bp.post('')
def create_location() -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    locations_service.create(location)
    return make_response(jsonify(location.put_into_dto()), HTTPStatus.CREATED)

@locations_bp.get('/<int:location_id>')
def get_location(location_id: int) -> Response:
    location = locations_service.find_by_id(location_id)
    if location:
        return make_response(jsonify(location.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)

@locations_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
    content = request.get_json()
    location = locations_service.find_by_id(location_id)
    if not location:
        return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)

    updated_location = Location.create_from_dto(content)
    locations_service.update(location_id, updated_location)
    return make_response(jsonify(updated_location.put_into_dto()), HTTPStatus.OK)

@locations_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:
    location = locations_service.find_by_id(location_id)
    if not location:
        return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)

    locations_service.delete(location_id)
    return make_response(jsonify({"message": "Location deleted successfully"}), HTTPStatus.NO_CONTENT)
