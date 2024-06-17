from core.repository.ieventsRepository import IEventsRepository

class GetAllEventsUseCase : 

    def __init__(self, repository: IEventsRepository) -> None:
        self.__repository = repository
    
    async def execute(self):
        events = await self.__repository.findAll();
        return events