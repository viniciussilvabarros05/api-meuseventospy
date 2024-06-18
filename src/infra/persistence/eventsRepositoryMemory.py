from src.core.repository.ieventsRepository import IEventsRepository
from typing import List
from prisma.models import Event
from prisma import Prisma
class EventRepositoryMemory(IEventsRepository):


    def __init__(self, repository: Event):
        self.__repository = repository

    
    async def create(self, event: Event):
        return await self.__repository.create(event)

    async def findAll(self) -> List[Event]:
        return self.__repository.find_many()

    async def getById(self, eventId: str, ) -> bool:
        return await self.__repository.getById(eventId)

    async def update(self, event: Event) -> None:
        return await self.__repository.update(event)

    async def delete(self, eventId: str) -> None:
        return await self.__repository.delete(eventId)
