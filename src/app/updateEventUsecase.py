from src.core.repository.ieventsRepository import IEventsRepository
class UpdateEventUseCase:

    def __init__(self, repository: IEventsRepository) -> None:
        self.__repository = repository

    async def execute(self, event:dict):
        result = await self.__repository.update(event)
        return result
    