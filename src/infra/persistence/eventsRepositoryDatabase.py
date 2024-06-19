from src.core.repository.ieventsRepository import IEventsRepository
from typing import List
from prisma import Prisma
from prisma.actions import EventActions
from prisma.errors import MissingRequiredValueError, RecordNotFoundError
from src.core.entity.event import Event


class EventRepositoryDatabase(IEventsRepository):

    def __init__(self, repository: EventActions):
        self.__repository = repository

    async def create(self, event: Event):
        try:
            self.__repository.create(data=event.get_event())
            return {
            "status": 200
            }
        except ValueError as e:
            return {"error": "Evento não pode ser criado"}
        except MissingRequiredValueError as e:
            return {"error": str(e)}

    async def findAll(self, id: str) -> List:
        events = self.__repository.find_many(where={
            "userId": id
        })
        print(events)
        return events

    async def getById(self, eventId: str, ) -> Event:
        try:
            event = self.__repository.find_unique_or_raise(
                where={
                    "id": eventId
                }
            )
            return event
        except RecordNotFoundError:
            return {"error": "Evento não encontrado"}

    async def update(self, event: Event) -> None:
        try:
            return self.__repository.update(
                where={
                    'id': event.id,
                },
                data=event
            )
        except ValueError:
            return {"error": "Evento não atualizado"}

    async def delete(self, eventId: str) -> dict:
        try:
            self.__repository.delete(
                where={
                    'id': eventId,
                })
            return {"status": True}
        except ValueError:
            return {"error": "Evento não encontrado"}
