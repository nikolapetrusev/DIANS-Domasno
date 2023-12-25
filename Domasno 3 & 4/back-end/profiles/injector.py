from injector import Injector

from profiles.modules import UserModule, ReviewModule


injector = Injector(
    [
        UserModule,
        ReviewModule,
    ]
)
