from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Sopla import Sopla
from my_project.auth.service.orders.SoplaService import SoplaService

sopla_service = SoplaService()
sopla_bp = Blueprint('sopla', __name__, url_prefix='/sopla')

@sopla_bp.get('')
def get_all_sopla() -> Response:
    soplas = sopla_service.find_all()
    soplas_dto = [sopla.put_into_dto() for sopla in soplas]
    return make_response(jsonify(soplas_dto), HTTPStatus.OK)

@sopla_bp.post('')
def create_sopla() -> Response:
    content = request.get_json()
    sopla = Sopla.create_from_dto(content)
    sopla_service.create(sopla)
    return make_response(jsonify(sopla.put_into_dto()), HTTPStatus.CREATED)

@sopla_bp.get('/<int:sopla_id>')
def get_sopla(sopla_id: int) -> Response:
    sopla = sopla_service.find_by_id(sopla_id)
    if sopla:
        return make_response(jsonify(sopla.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Sopla not found"}), HTTPStatus.NOT_FOUND)

@sopla_bp.put('/<int:sopla_id>')
def update_sopla(sopla_id: int) -> Response:
    content = request.get_json()
    sopla = sopla_service.find_by_id(sopla_id)
    if not sopla:
        return make_response(jsonify({"error": "Sopla not found"}), HTTPStatus.NOT_FOUND)

    updated_sopla = Sopla.create_from_dto(content)
    sopla_service.update(sopla_id, updated_sopla)
    return make_response(jsonify(updated_sopla.put_into_dto()), HTTPStatus.OK)

@sopla_bp.delete('/<int:sopla_id>')
def delete_sopla(sopla_id: int) -> Response:
    sopla = sopla_service.find_by_id(sopla_id)
    if not sopla:
        return make_response(jsonify({"error": "Sopla not found"}), HTTPStatus.NOT_FOUND)

    sopla_service.delete(sopla_id)
    return make_response(jsonify({"message": "Sopla deleted successfully"}), HTTPStatus.NO_CONTENT)
