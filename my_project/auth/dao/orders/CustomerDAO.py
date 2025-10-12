from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Customers import Customer

class CustomerDAO(GeneralDAO):
    _domain_type = Customer

    def create(self, customer: Customer) -> None:
        self._session.add(customer)
        self._session.commit()

    def find_all(self) -> List[Customer]:
        return self._session.query(Customer).all()

    def find_by_id(self, customer_id: int) -> Optional[Customer]:
        return self._session.query(Customer).filter(Customer.id == customer_id).first()
