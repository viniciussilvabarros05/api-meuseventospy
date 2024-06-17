from src.core.entity.user import User
from abc import ABC, abstractmethod
from typing import List

class IUserRepository(ABC):
    @abstractmethod
    async def create(self, event: User) -> None:
        pass

    @abstractmethod
    async def getById(self, user_id: str, friend_id: str) -> User:
        pass
    @abstractmethod
    async def delete(eventId:str) -> None:
        pass

