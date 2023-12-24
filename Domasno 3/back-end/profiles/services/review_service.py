from injector import inject

from metaclasses import SingletonMeta

from profiles.services.interfaces import IReviewService


class ReviewService(metaclass=SingletonMeta):
    @inject
    def __init__(self, service: IReviewService) -> None:
        self.execute = service
