from injector import Injector

from app.modules import CityModule, WineryModule


injector = Injector(
    [
        CityModule,
        WineryModule,
    ]
)
