from injector import Module, Binder, singleton

from profiles.services import UserService, ReviewService
from profiles.services.implementations import UserServiceImpl, ReviewServiceImpl


class UserModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(UserService, to=UserServiceImpl, scope=singleton)


class ReviewModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ReviewService, to=ReviewServiceImpl, scope=singleton)
