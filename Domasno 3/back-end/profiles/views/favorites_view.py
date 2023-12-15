import json
from typing import Any

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from profiles.services import UserService, FavoritesService


class FavoritesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None) -> Response:
        """
        Get favorite wineries.
        Parameters:
            N/A
        Returns:
            data: dict[str, Any]
        """
        user = UserService.get_user(request.user)

        data: dict[str, Any] = {}
        data["favorites"] = FavoritesService.get_favorite(user)

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """
        Add winery to favorites.

        Parameters:
            winery_id: int
        Returns:
            status 200 OK
        """
        user = UserService.get_user(request.user)

        # w_id = request.POST["winery_id"]
        data = json.loads(request.body.decode("utf-8"))

        FavoritesService.add_favorite(user, data)

        return Response(status=status.HTTP_202_ACCEPTED)
