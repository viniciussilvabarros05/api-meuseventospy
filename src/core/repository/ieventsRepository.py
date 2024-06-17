from src.core.entity.event import Event
from abc import ABC, abstractmethod
from typing import List

class IEventsRepository(ABC):
    @abstractmethod
    async def create(self, event: Event) -> None:
        pass

    @abstractmethod
    async def getById(self, eventId: str) -> Event:
        pass
    @abstractmethod
    async def findAll(self)-> List[Event]:
        pass
    @abstractmethod
    async def update(self,event:Event) -> None:
        pass
    
    @abstractmethod
    async def delete(self, eventId:str) -> None:
        pass

