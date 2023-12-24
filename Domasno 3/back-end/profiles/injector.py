from injector import Injector

from profiles.modules import UserServiceModule


injector = Injector(
    [
        UserServiceModule,
    ]
)