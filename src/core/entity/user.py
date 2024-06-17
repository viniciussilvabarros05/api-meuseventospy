import uuid

class User:
    def __init__(self, email: str, name: str = None):
        self.__id = str(uuid.uuid4())
        self.__email = email
        self.__name = name

    def get_user(self):
        return self
