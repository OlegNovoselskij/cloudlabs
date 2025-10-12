from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.SensorsType import SensorType
from sqlalchemy.orm import joinedload

class SensorTypeDAO(GeneralDAO):
    _domain_type = SensorType

    def create(self, sensor_type: SensorType) -> None:
        self._session.add(sensor_type)
        self._session.commit()

    def find_all(self) -> List[SensorType]:
        return self._session.query(SensorType).all()

    def find_all_expanded(self) -> list:
        query = (
            self._session.query(SensorType)
            .options(joinedload(SensorType.sensors))
        )
        result = []
        for st in query.all():
            result.append({
                "id": st.id,
                "name": st.name,
                "description": st.description,
                "sensors": [
                    {
                        "id": s.id,
                        "installation_date": str(s.installation_date),
                        "type_id": s.type_id
                    } for s in st.sensors
                ]
            })
        return result

    def find_by_id(self, sensor_type_id: int) -> Optional[SensorType]:
        return self._session.query(SensorType).filter(SensorType.sensor_type_id == sensor_type_id).first()
