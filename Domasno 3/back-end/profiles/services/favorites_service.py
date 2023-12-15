from typing import Any

from django.contrib.auth.models import User

from app.models import Winery
from app.serializers import WinerySerializer


class FavoritesService:
    @staticmethod
    def get_favorite(user: User) -> dict[str, Any]:
        favorites = fav if (fav := user.extended.favorites) else []
        return WinerySerializer(favorites, many=True).data

    @staticmethod
    def add_favorite(user: User, data: dict[str, Any]) -> None:
        user.extended.favorites.add(Winery.objects.get(pk=data["winery_id"]))
