from typing import List, Optional
from my_project.auth.domain.orders.SensorsCoordinates import SensorsCoordinates
from my_project.auth.dao.general_dao import GeneralDAO
from sqlalchemy.orm import joinedload

class SensorsCoordinatesDAO(GeneralDAO):
    def create(self, sensor_coordinate: SensorsCoordinates) -> None:
        self._session.add(sensor_coordinate)
        self._session.commit()

    def find_all(self) -> List[SensorsCoordinates]:
        return self._session.query(SensorsCoordinates).all()

    def find_all_expanded(self) -> list:
        query = (
            self._session.query(SensorsCoordinates)
            .options(joinedload(SensorsCoordinates.sensor), joinedload(SensorsCoordinates.coordinate))
        )
        result = []
        for record in query.all():
            result.append({
                "sensors_coordinate": {
                    "sensor_id": record.sensor_id,
                    "coordinate_id": record.coordinate_id
                },
                "sensor": {
                    "id": record.sensor.id,
                    "installation_date": str(record.sensor.installation_date),
                    "type_id": record.sensor.type_id
                },
                "coordinate": {
                    "id": record.coordinate.id,
                    "latitude": record.coordinate.latitude,
                    "longitude": record.coordinate.longitude
                }
            })
        return result

    def find_by_id(self, sensor_id: int, coordinate_id: int) -> Optional[SensorsCoordinates]:
        return self._session.query(SensorsCoordinates).filter(
            SensorsCoordinates.sensor_id == sensor_id,
            SensorsCoordinates.coordinate_id == coordinate_id
        ).first()

    def find_by_sensor_id(self, sensor_id: int) -> List[SensorsCoordinates]:
        return self._session.query(SensorsCoordinates).filter(
            SensorsCoordinates.sensor_id == sensor_id
        ).all()

    def find_by_coordinate_id(self, coordinate_id: int) -> List[SensorsCoordinates]:
        return self._session.query(SensorsCoordinates).filter(
            SensorsCoordinates.coordinate_id == coordinate_id
        ).all()

    def update(self, sensor_coordinate: SensorsCoordinates) -> None:
        self._session.merge(sensor_coordinate)
        self._session.commit()

    def delete(self, sensor_id: int, coordinate_id: int) -> None:
        sensor_coordinate = self.find_by_id(sensor_id, coordinate_id)
        if sensor_coordinate:
            self._session.delete(sensor_coordinate)
            self._session.commit() 