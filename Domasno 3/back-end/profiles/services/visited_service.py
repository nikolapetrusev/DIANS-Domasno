from typing import Any

from django.contrib.auth.models import User

from app.models import Winery
from app.serializers import WinerySerializer


class VisitedService:
    @staticmethod
    def get_visited(user: User) -> dict[str, Any]:
        visited = vis if (vis := user.extended.visited) else []
        return WinerySerializer(visited, many=True).data

    @staticmethod
    def add_visited(user: User, data: dict[str, Any]) -> None:
        user.extended.visited.add(Winery.objects.get(pk=data["winery_id"]))
