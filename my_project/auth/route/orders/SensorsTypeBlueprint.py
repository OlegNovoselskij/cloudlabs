from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.domain.orders.SensorsType import SensorType
from my_project.auth.service.orders.SensorsTypeService import SensorsTypeService

sensorstype_service = SensorsTypeService()
sensors_type_bp = Blueprint('sensorstype', __name__, url_prefix='/sensorstype')

@sensors_type_bp.get('')
def get_all_sensorstypes() -> Response:
    sensorstypes = sensorstype_service.find_all()
    sensorstypes_dto = [stype.put_into_dto() for stype in sensorstypes]
    return make_response(jsonify(sensorstypes_dto), HTTPStatus.OK)

@sensors_type_bp.post('')
def create_sensorstype() -> Response:
    content = request.get_json()
    sensorstype = SensorType.create_from_dto(content)
    sensorstype_service.create(sensorstype)
    return make_response(jsonify(sensorstype.put_into_dto()), HTTPStatus.CREATED)

@sensors_type_bp.get('/<int:sensor_type_id>')
def get_sensorstype(sensor_type_id: int) -> Response:
    sensorstype = sensorstype_service.find_by_id(sensor_type_id)
    if sensorstype:
        return make_response(jsonify(sensorstype.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "SensorType not found"}), HTTPStatus.NOT_FOUND)

@sensors_type_bp.put('/<int:sensor_type_id>')
def update_sensorstype(sensor_type_id: int) -> Response:
    content = request.get_json()
    sensorstype = sensorstype_service.find_by_id(sensor_type_id)
    if not sensorstype:
        return make_response(jsonify({"error": "SensorType not found"}), HTTPStatus.NOT_FOUND)

    updated_sensorstype = SensorType.create_from_dto(content)
    updated_sensorstype.sensor_type_id = sensor_type_id
    sensorstype_service.update(updated_sensorstype)
    return make_response(jsonify(updated_sensorstype.put_into_dto()), HTTPStatus.OK)

@sensors_type_bp.delete('/<int:sensor_type_id>')
def delete_sensorstype(sensor_type_id: int) -> Response:
    sensorstype = sensorstype_service.find_by_id(sensor_type_id)
    if not sensorstype:
        return make_response(jsonify({"error": "SensorType not found"}), HTTPStatus.NOT_FOUND)

    sensorstype_service.delete(sensor_type_id)
    return make_response(jsonify({"message": "SensorType deleted successfully"}), HTTPStatus.NO_CONTENT)

@sensors_type_bp.get('/<int:type_id>/sensors')
def get_sensors_by_type(type_id: int) -> Response:
    from my_project.auth.service.orders.SensorsService import SensorsService
    sensors_service = SensorsService()
    sensors = sensors_service.get_by_type_id(type_id)
    sensors_dto = [sensor.put_into_dto() for sensor in sensors]
    return make_response(jsonify(sensors_dto), HTTPStatus.OK)

@sensors_type_bp.get('/expanded')
def get_all_sensorstypes_expanded() -> Response:
    data = sensorstype_service.get_all_expanded()
    return make_response(jsonify(data), HTTPStatus.OK)
