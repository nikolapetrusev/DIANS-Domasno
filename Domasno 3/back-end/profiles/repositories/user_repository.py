from django.contrib.auth.models import User

from app.models import Winery


class UserRepository:
    def get_user(username: str) -> User:
        return User.objects.get(username=username)

    def get_favorites(user: User) -> list[Winery]:
        return fav if (fav := user.extended.favorites) else []

    def add_favorite(user: User, winery: Winery) -> None:
        user.extended.favorites.add(winery)

    def get_visited(user: User) -> list[Winery]:
        return vis if (vis := user.extended.visited) else []

    def add_visited(user: User, winery: Winery) -> None:
        user.extended.visited.add(winery)
