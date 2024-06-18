from src.core.repository.ieventsRepository import IEventsRepository
class GetAllEventsUseCase:

    def __init__(self, repository: IEventsRepository) -> None:
        self.__repository = repository

    async def execute(self, id:str):
        events = await self.__repository.findAll(id)
        return events
    