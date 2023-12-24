import json
from typing import Any
from injector import Injector
# from profiles.injector import Injector

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from profiles.services import UserService
from profiles.modules import UserServiceModule
from profiles.services.interfaces import IUserService

class FavoritesView(APIView):
    # View can only be accessed if user is authenticated
    permission_classes = (IsAuthenticated,)
    # Necessary services
    injector = Injector(UserServiceModule)
    user_service = injector.get(IUserService)
    # user_service = UserService()

    def get(self, request, format=None) -> Response:
        """
        Get favorite wineries.
        Parameters:
            N/A
        Returns:
            data: dict[str, Any]
        """
        data: dict[str, Any] = {}
        data["favorites"] = self.user_service.get_favorites(request.user)

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """
        Add winery to favorites.

        Parameters:
            winery_id: int
        Returns:
            status 200 OK
        """
        data = json.loads(request.body.decode("utf-8"))
        self.user_service.add_favorite(request.user, data)

        return Response(status=status.HTTP_202_ACCEPTED)
