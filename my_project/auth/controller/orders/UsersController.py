from typing import List
from my_project.auth.dao.orders.UsersDAO import UsersDAO
from my_project.auth.domain.orders.Users import User

class UsersController:
    _dao = UsersDAO()

    @classmethod
    def find_all(cls) -> List[User]:
        return cls._dao.find_all()

    def create(self, user: User) -> None:
        self._dao.create(user)

    def find_by_id(self, user_id: int) -> User:
        return self._dao.find_by_id(user_id)

    def update(self, user_id: int, user: User) -> None:
        self._dao.update(user_id, user)

    def delete(self, user_id: int) -> None:
        self._dao.delete(user_id)
