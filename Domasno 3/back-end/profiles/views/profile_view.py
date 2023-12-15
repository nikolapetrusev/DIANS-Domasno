import json
from typing import Any

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from profiles.serializers import ProfileUserSerializer
from profiles.services import UserService
from profiles.exceptions import PasswordsDontMatchError


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None) -> Response:
        """
        Get user details
        Parameters:
            N/A
        """
        data: dict[str, Any] = {}

        user = UserService.get_user(request.user)
        # data["user"] = UserSerializer(user).data
        data["user"] = ProfileUserSerializer(user).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """
        Add review for winery
        Parameters:
            winery_id: int
            rating: int
            comment: str | None
        """
        user = UserService.get_user(request.user)
        data = json.loads(request.body.decode("utf-8"))

        try:
            UserService.update_user(user, data)
        except PasswordsDontMatchError as err:
            return Response(
                data={"data": str(err)}, status=status.HTTP_406_NOT_ACCEPTABLE
            )

        return Response(status=status.HTTP_200_OK)
