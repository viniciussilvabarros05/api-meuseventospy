from src.core.repository.ieventsRepository import IEventsRepository
from typing import List
from prisma import Prisma
from prisma.models import Event


class EventRepositoryDatabase(IEventsRepository):

    def __init__(self, repository: Prisma):
        self.__repository = repository

    async def create(self, event: Event):
        try:
            return self.__repository.create(data=event)
        except e:
            return {"error": "Evento não pode ser criado"}

    async def findAll(self, id: str) -> List[Event]:
        events = self.__repository.event.find_many(where={
            "userId": id
        })
        return events

    async def getById(self, eventId: str, ) -> Event:
        try:
            event = self.__repository.event.find_unique_or_raise(
                where={
                    "id": eventId
                }
            )
            return event
        except e:
            return {"error": "Evento não encontrado"}

    async def update(self, event: Event) -> None:
        try:
            return self.__repository.update(
                where={
                    'id': event.id,
                },
                data=event
            )
        except e:
            return {"error": "Evento não atualizado"}

    async def delete(self, eventId: str) -> None:
        try:
            self.__repository.delete(
                where={
                    'id': eventId,
                })
        except e:
            return {"error": "Evento não encontrado"}
