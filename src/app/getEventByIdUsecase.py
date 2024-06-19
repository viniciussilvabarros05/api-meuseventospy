from src.core.repository.ieventsRepository import IEventsRepository
class GetEventByIdUseCase:

    def __init__(self, repository: IEventsRepository) -> None:
        self.__repository = repository

    async def execute(self, eventId:str):
        events = await self.__repository.getById(eventId)
        return events
    