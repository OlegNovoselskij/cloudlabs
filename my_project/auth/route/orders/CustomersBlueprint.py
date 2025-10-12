from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.Customers import Customer
from my_project.auth.service.orders.CustomersService import CustomersService

customers_service = CustomersService()
customers_bp = Blueprint('customers', __name__, url_prefix='/customers')

@customers_bp.get('')
def get_all_customers() -> Response:
    customers = customers_service.find_all()
    customers_dto = [customer.put_into_dto() for customer in customers]
    return make_response(jsonify(customers_dto), HTTPStatus.OK)

@customers_bp.post('')
def create_customer() -> Response:
    content = request.get_json()
    customer = Customer.create_from_dto(content)
    customers_service.create(customer)
    return make_response(jsonify(customer.put_into_dto()), HTTPStatus.CREATED)

@customers_bp.get('/<int:customer_id>')
def get_customer(customer_id: int) -> Response:
    customer = customers_service.find_by_id(customer_id)
    if customer:
        return make_response(jsonify(customer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Customer not found"}), HTTPStatus.NOT_FOUND)

@customers_bp.put('/<int:customer_id>')
def update_customer(customer_id: int) -> Response:
    content = request.get_json()
    customer = customers_service.find_by_id(customer_id)
    if not customer:
        return make_response(jsonify({"error": "Customer not found"}), HTTPStatus.NOT_FOUND)

    updated_customer = Customer.create_from_dto(content)
    updated_customer.customer_id = customer_id
    customers_service.update(updated_customer)
    return make_response(jsonify(updated_customer.put_into_dto()), HTTPStatus.OK)

@customers_bp.delete('/<int:customer_id>')
def delete_customer(customer_id: int) -> Response:
    customer = customers_service.find_by_id(customer_id)
    if not customer:
        return make_response(jsonify({"error": "Customer not found"}), HTTPStatus.NOT_FOUND)

    customers_service.delete(customer_id)
    return make_response(jsonify({"message": "Customer deleted successfully"}), HTTPStatus.NO_CONTENT)
