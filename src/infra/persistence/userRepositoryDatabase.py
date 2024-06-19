from src.core.repository.iuserRepository import IUserRepository
from src.core.entity.user import User
from prisma.actions import UserActions
from prisma.errors import UniqueViolationError


class UserRepositoryDatabase(IUserRepository):
    def __init__(self, repository: UserActions):
        self.__repository = repository

    async def create(self, user: User):
        try:
            if not user:
                raise ValueError("Nenhum dado fornecido")

            if not user.get_email():
                raise ValueError("Email dado fornecido")

            if not user.get_name():
                raise ValueError("Nome não fornecido")

            self.__repository.create(data=user.get_user())
            return {
                "status": 200
            }

        except UniqueViolationError as e:
            return {"error": str(e)},
        except ValueError as e:
            return {"error": str(e)}

    async def getById(self, id: str, ) -> User:
        return self.__repository.find_unique(
            where={
                'id': id,
            },
            include={
                'event': True
            }
        )

    async def delete(self, id: str) -> None:
        return self.__repository.delete(id)
