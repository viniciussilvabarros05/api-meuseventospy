from src.core.repository.iuserRepository import IUserRepository
class GetUserByEmailUseCase:

    def __init__(self, repository: IUserRepository) -> None:
        self.__repository = repository

    async def execute(self, id:str):
        events = await self.__repository.getById(id)
        return events
    