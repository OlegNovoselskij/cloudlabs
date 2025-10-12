from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Pumps import Pump
from my_project.auth.service.orders.PumpsService import PumpsService

pumps_service = PumpsService()
pumps_bp = Blueprint('pumps', __name__, url_prefix='/pumps')

@pumps_bp.get('')
def get_all_pumps() -> Response:
    pumps = pumps_service.find_all()
    pumps_dto = [pump.put_into_dto() for pump in pumps]
    return make_response(jsonify(pumps_dto), HTTPStatus.OK)

@pumps_bp.post('')
def create_pump() -> Response:
    content = request.get_json()
    pump = Pump.create_from_dto(content)
    pumps_service.create(pump)
    return make_response(jsonify(pump.put_into_dto()), HTTPStatus.CREATED)

@pumps_bp.get('/<int:pump_id>')
def get_pump(pump_id: int) -> Response:
    pump = pumps_service.find_by_id(pump_id)
    if pump:
        return make_response(jsonify(pump.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Pump not found"}), HTTPStatus.NOT_FOUND)

@pumps_bp.put('/<int:pump_id>')
def update_pump(pump_id: int) -> Response:
    content = request.get_json()
    pump = pumps_service.find_by_id(pump_id)
    if not pump:
        return make_response(jsonify({"error": "Pump not found"}), HTTPStatus.NOT_FOUND)

    updated_pump = Pump.create_from_dto(content)
    pumps_service.update(pump_id, updated_pump)
    return make_response(jsonify(updated_pump.put_into_dto()), HTTPStatus.OK)

@pumps_bp.delete('/<int:pump_id>')
def delete_pump(pump_id: int) -> Response:
    pump = pumps_service.find_by_id(pump_id)
    if not pump:
        return make_response(jsonify({"error": "Pump not found"}), HTTPStatus.NOT_FOUND)

    pumps_service.delete(pump_id)
    return make_response(jsonify({"message": "Pump deleted successfully"}), HTTPStatus.NO_CONTENT)
