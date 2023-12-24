from injector import Module, Binder, singleton

from app.services import CityService, WineryService
from app.services.implementations import CityServiceImpl, WineryServiceImpl


class CityModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(CityService, to=CityServiceImpl, scope=singleton)


class WineryModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(WineryService, to=WineryServiceImpl, scope=singleton)
