from src.core.repository.ieventsRepository import IEventsRepository
from src.core.entity.event import Event
class CreateEventUsecase:

    def __init__(self, repository: IEventsRepository) -> None:
        self.__repository = repository

    async def execute(self, event: Event):
        user = await self.__repository.create(event)
        return user
    