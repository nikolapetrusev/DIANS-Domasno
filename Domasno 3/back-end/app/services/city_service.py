from typing import Any

from app.models import City
from app.serializers import CitySerializer
from app.exceptions import CityNotFoundError


class CityService:
    @staticmethod
    def get_city_by_id(city_id: int) -> dict[str, City]:
        if city := City.objects.get(pk=city_id):
            return {"city": CitySerializer(city).data}
        raise CityNotFoundError(city_id)

    @staticmethod
    def get_all_cities() -> dict[str, list[City]]:
        if cities := City.objects.all().order_by("name"):
            return {"data": CitySerializer(cities, many=True).data}
        return {"data": []}

    @staticmethod
    def get_cities(data: dict[str, Any]) -> dict[str, City] | dict[str, list[City]]:
        """
        Return city by id if city_id is provided in request
        Else return all cities

        Parameters <dict[str, Any]>:
            city_id: int | None
        """
        if city_id := data.get("city_id", None):
            return CityService.get_city_by_id(city_id)
        else:
            return CityService.get_all_cities()
