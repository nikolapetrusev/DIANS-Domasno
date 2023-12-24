import json
from typing import Any
from injector import Injector

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from profiles.services import UserService


class VisitedView(APIView):
    # View can only be accessed if user is authenticated
    permission_classes = (IsAuthenticated,)
    # Necessary services
    injector = Injector()
    user_service = injector.get(UserService)
    # user_service = UserService()

    def get(self, request, format=None) -> Response:
        """
        Get visited wineries.
        Parameters:
            N/A
        Returns:
            data: dict[str, Any]
        """
        data: dict[str, Any] = {}
        data["visited"] = self.user_service.execute.get_visited(request.user)

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """
        Add winery to visited.

        Parameters:
            winery_id: int
        Returns:
            status 200 OK
        """
        data = json.loads(request.body.decode("utf-8"))
        self.user_service.execute.add_visited(request.user, data)

        return Response(status=status.HTTP_202_ACCEPTED)
