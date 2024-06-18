from src.core.repository.iuserRepository import IUserRepository
from src.core.entity.user import User
from prisma import Prisma
from prisma.errors import DataError 
class UserRepositoryDatabase(IUserRepository):
    def __init__(self, repository: Prisma):
        self.__repository = repository

    async def create(self, user: User):
        try: 
            if not user:
                raise ValueError("Nenhum dado fornecido")
            
            if not user.get_email():
                raise ValueError("Email dado fornecido")
            
            if not user.get_name():
                raise ValueError("Nome não fornecido")
            
            self.__repository.user.create(data=user.get_user())
            return {
                "status" : 200
            }

        except DataError as e: 
            return {"error":str(e), "status": 400}, 

    async def getById(self, id: str, ) -> User:
        return self.__repository.getById(id)

    async def delete(self, id: str) -> None:
        return  self.__repository.delete(id)
