from typing import Any
from app.models import Winery
from app.serializers import WinerySerializer
from app.exceptions import WineryNotFoundError


class WineryService:
    @staticmethod
    def get_winery_by_id(winery_id: int) -> dict[str, Winery]:
        if winery := Winery.objects.get(pk=winery_id):
            return {"winery": WinerySerializer(winery).data}
        else:
            raise WineryNotFoundError(winery_id)

    @staticmethod
    def get_wineries_by_city(city_id: int) -> dict[str, list[Winery]]:
        if wineries := Winery.objects.filter(city__pk=city_id):
            return {"wineries": WinerySerializer(wineries, many=True).data}
        else:
            return {"wineries": []}

    @staticmethod
    def get_all_wineries() -> dict[str, list[Winery]]:
        if wineries := Winery.objects.all():
            return {"wineries": WinerySerializer(wineries, many=True).data}
        return {"wineries": []}

    @staticmethod
    def get_wineries(
        data: dict[str, Any]
    ) -> dict[str, Winery] | dict[str, list[Winery]]:
        # Return by winery id
        if winery_id := data.get("winery_id", None):
            return WineryService.get_winery_by_id(winery_id)
        # Return by city id
        elif city_id := data.get("city_id", None):
            return WineryService.get_wineries_by_city(city_id)
        # Return all
        else:
            return WineryService.get_all_wineries()
