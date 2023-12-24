from typing import Any
from app.models import Winery
from app.serializers import WinerySerializer
from app.exceptions import WineryNotFoundError
from app.repositories import WineryRepository
from metaclasses import SingletonMeta


class WineryService(metaclass=SingletonMeta):
    winery_repository = WineryRepository

    def get_winery_by_id(self, winery_id: int) -> dict[str, Winery]:
        if winery := self.winery_repository.get_winery_by_id(winery_id):
            return {"winery": WinerySerializer(winery).data}
        else:
            raise WineryNotFoundError(winery_id)

    def get_wineries_by_city(self, city_id: int) -> dict[str, list[Winery]]:
        if wineries := self.winery_repository.get_wineries_by_city(city_id):
            return {"wineries": WinerySerializer(wineries, many=True).data}
        else:
            return {"wineries": []}

    def get_all_wineries(self) -> dict[str, list[Winery]]:
        if wineries := self.winery_repository.get_all_wineries():
            return {"wineries": WinerySerializer(wineries, many=True).data}
        return {"wineries": []}

    def get_wineries(
        self,
        data: dict[str, Any],
    ) -> dict[str, Winery] | dict[str, list[Winery]]:
        # Return by winery id
        if winery_id := data.get("winery_id", None):
            return self.get_winery_by_id(winery_id)
        # Return by city id
        elif city_id := data.get("city_id", None):
            return self.get_wineries_by_city(city_id)
        # Return all
        else:
            return self.get_all_wineries()
