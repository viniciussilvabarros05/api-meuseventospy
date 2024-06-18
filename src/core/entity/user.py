import uuid

class User:
    def __init__(self, email: str, name: str = None):
        self.__id = str(uuid.uuid4())
        self.__email = email
        self.__name = name

    def get_email(self):
        return self.__email
    def get_name(self):
        return self.__name

    def get_user(self):
        return {
            "id" : self.__id,
            "email" : self.__email,
            "name" : self.__name,

        }