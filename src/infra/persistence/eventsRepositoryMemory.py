from src.core.repository.ieventsRepository import IEventsRepository
from src.core.entity.event import Event
from typing import List

class EventRepositoryMemory(IEventsRepository):
    repository: IEventsRepository

    def __init__(self, repository: IEventsRepository):
        self.__repository = repository

    async def create(self, event: Event):
        return await self.__repository.create(event)

    async def findAll(self) -> List[Event]:
        return await self.__repository.findAll()

    async def getById(self, eventId: str, ) -> bool:
        return await self.__repository.getById(eventId)

    async def update(self, event: Event) -> None:
        return await self.__repository.update(event)

    async def delete(self, eventId: str) -> None:
        return await self.__repository.delete(eventId)
