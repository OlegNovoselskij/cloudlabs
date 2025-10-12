from typing import List
from my_project.auth.dao.orders.CustomersDAO import CustomersDAO
from my_project.auth.domain.orders.Customers import Customer

class CustomersController:
    _dao = CustomersDAO()

    @classmethod
    def find_all(cls) -> List[Customer]:
        return cls._dao.find_all()

    def create(self, customer: Customer) -> None:
        self._dao.create(customer)

    def find_by_id(self, customer_id: int) -> Customer:
        return self._dao.find_by_id(customer_id)

    def update(self, customer_id: int, customer: Customer) -> None:
        self._dao.update(customer_id, customer)

    def delete(self, customer_id: int) -> None:
        self._dao.delete(customer_id)
