from core.repository.iuserRepository import IUserRepository
from core.entity.user import User


class UserRepositoryDatabase(IUserRepository):
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    async def create(self, user: User):
        return await self.__repository.create(user)

    async def getById(self, id: str, ) -> User:
        return await self.__repository.getById(id)

    async def update(self, user: User) -> None:
        return await self.__repository.update(user)

    async def delete(self, id: str) -> None:
        return await self.__repository.delete(id)
