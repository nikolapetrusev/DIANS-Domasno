from injector import Module, Binder, singleton

from profiles.services.interfaces import IUserService
from profiles.services.implementations import UserServiceImpl
from profiles.services import UserService


class UserServiceModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IUserService, to=UserServiceImpl, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)
