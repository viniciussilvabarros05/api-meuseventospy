from src.core.repository.iuserRepository import IUserRepository
from src.core.entity.user import User
class CreateUserUsecase:

    def __init__(self, repository: IUserRepository) -> None:
        self.__repository = repository

    async def execute(self, user: User):
        user = await self.__repository.create(user)
        return user
    