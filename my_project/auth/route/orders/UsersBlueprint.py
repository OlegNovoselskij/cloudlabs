from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Users import User
from my_project.auth.service.orders.UsersService import UsersService

users_service = UsersService()
users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.get('')
def get_all_users() -> Response:
    users = users_service.find_all()
    users_dto = [user.put_into_dto() for user in users]
    return make_response(jsonify(users_dto), HTTPStatus.OK)

@users_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    users_service.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@users_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    user = users_service.find_by_id(user_id)
    if user:
        return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

@users_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = users_service.find_by_id(user_id)
    if not user:
        return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

    updated_user = User.create_from_dto(content)
    updated_user.user_id = user_id
    users_service.update(updated_user)
    return make_response(jsonify(updated_user.put_into_dto()), HTTPStatus.OK)

@users_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user = users_service.find_by_id(user_id)
    if not user:
        return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

    users_service.delete(user_id)
    return make_response(jsonify({"message": "User deleted successfully"}), HTTPStatus.NO_CONTENT)
