from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Users import User

class UserDAO(GeneralDAO):
    _domain_type = User

    def create(self, user: User) -> None:
        self._session.add(user)
        self._session.commit()

    def find_all(self) -> List[User]:
        return self._session.query(User).all()

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._session.query(User).filter(User.id == user_id).first()
