from src.core.entity.event import Event
from abc import ABC, abstractmethod
from typing import List

class IEventsRepository(ABC):
    @abstractmethod
    async def create(event: Event) -> None:
        pass

    @abstractmethod
    async def getById(eventId: str) -> Event:
        pass
    @abstractmethod
    async def findAll()-> List[Event]:
        pass
    @abstractmethod
    async def update(event:Event) -> None:
        pass
    
    @abstractmethod
    async def delete(eventId:str) -> None:
        pass

