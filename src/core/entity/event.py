import uuid
from datetime import datetime
from typing import List, TypedDict


class EventProps(TypedDict):
    userId: str
    name: str
    date: str
    talks: List[str]
    dist: List[str]
    local: str


class Event:
    def __init__(self, event_props: EventProps):
        self.__id = str(uuid.uuid4())
        self.__name = event_props.get('name')
        self.__date = event_props.get('date')
        self.__talks = event_props.get('talks', [])
        self.__dist = event_props.get('dist', [])
        self.__local = event_props.get('local')
        self.__createdAt = datetime.now()
        self.__userId = event_props.get('userId')

    def get_event(self):
        return self

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    @property
    def talks(self):
        return self.__talks

    @property
    def dist(self):
        return self.__dist

    @property
    def local(self):
        return self.__local

    @property
    def createdAt(self):
        return self.__createdAt

    @property
    def userId(self):
        return self.__userId

    def get_event(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "name": self.name,
            "date":self.date,
            "talks": self.talks,
            "dist" : self.dist,
            "local": self.local  
        }
