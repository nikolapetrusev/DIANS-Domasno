from injector import inject

from metaclasses import SingletonMeta

from profiles.services.interfaces import IUserService


class UserService(metaclass=SingletonMeta):
    @inject
    def __init__(self, service: IUserService) -> None:
        self.execute = service