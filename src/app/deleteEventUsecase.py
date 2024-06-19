from src.core.repository.ieventsRepository import IEventsRepository
class DeleteEventUseCase:

    def __init__(self, repository: IEventsRepository) -> None:
        self.__repository = repository

    async def execute(self, eventId:str):
        events = await self.__repository.delete(eventId)
        return events
    