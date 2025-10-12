from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.PumpOperations import PumpOperation
from my_project.auth.service.orders.PumpOperationsService import PumpOperationsService

pumpoperations_service = PumpOperationsService()
pump_operations_bp = Blueprint('pumpoperations', __name__, url_prefix='/pumpoperations')

@pump_operations_bp.get('')
def get_all_pumpoperations() -> Response:
    pumpoperations = pumpoperations_service.find_all()
    pumpoperations_dto = [po.put_into_dto() for po in pumpoperations]
    return make_response(jsonify(pumpoperations_dto), HTTPStatus.OK)

@pump_operations_bp.post('')
def create_pumpoperation() -> Response:
    content = request.get_json()
    pumpoperation = PumpOperation.create_from_dto(content)
    pumpoperations_service.create(pumpoperation)
    return make_response(jsonify(pumpoperation.put_into_dto()), HTTPStatus.CREATED)

@pump_operations_bp.get('/<int:pump_operation_id>')
def get_pumpoperation(pump_operation_id: int) -> Response:
    pumpoperation = pumpoperations_service.find_by_id(pump_operation_id)
    if pumpoperation:
        return make_response(jsonify(pumpoperation.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "PumpOperation not found"}), HTTPStatus.NOT_FOUND)

@pump_operations_bp.put('/<int:pump_operation_id>')
def update_pumpoperation(pump_operation_id: int) -> Response:
    content = request.get_json()
    pumpoperation = pumpoperations_service.find_by_id(pump_operation_id)
    if not pumpoperation:
        return make_response(jsonify({"error": "PumpOperation not found"}), HTTPStatus.NOT_FOUND)

    updated_pumpoperation = PumpOperation.create_from_dto(content)
    updated_pumpoperation.pump_operation_id = pump_operation_id
    pumpoperations_service.update(updated_pumpoperation)
    return make_response(jsonify(updated_pumpoperation.put_into_dto()), HTTPStatus.OK)

@pump_operations_bp.delete('/<int:pump_operation_id>')
def delete_pumpoperation(pump_operation_id: int) -> Response:
    pumpoperation = pumpoperations_service.find_by_id(pump_operation_id)
    if not pumpoperation:
        return make_response(jsonify({"error": "PumpOperation not found"}), HTTPStatus.NOT_FOUND)

    pumpoperations_service.delete(pump_operation_id)
    return make_response(jsonify({"message": "PumpOperation deleted successfully"}), HTTPStatus.NO_CONTENT)
