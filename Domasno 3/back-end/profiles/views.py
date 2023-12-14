import json
from typing import Any

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.models import Winery, Review
from profiles.serializers import ProfileUserSerializer
from profiles.services import UserService, ReviewService, FavoritesService
from profiles.exceptions import InvalidInputError, PasswordsDontMatchError


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
        user = User.objects.get(username=request.user)

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
        user = User.objects.get(username=request.user)

        # w_id = request.POST["winery_id"]
        data = json.loads(request.body.decode("utf-8"))
        
        FavoritesService.add_favorite(user, data)

        return Response(status=status.HTTP_202_ACCEPTED)


class ReviewsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None) -> Response:
        """
        Add review for winery
        Parameters:
            winery_id: int
            rating: float
            comment: str | None
        """
        user = User.objects.get(username=request.user)
        data = json.loads(request.body.decode("utf-8"))

        ReviewService.create_review(user, data)
        
        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, format=None) -> Response:
        """
        Edit review
        Parameters:
            review_id: int
            winery_id: int
            rating: float
            comment: str
        """
        user = User.objects.get(username=request.user)

        try:
            ReviewService.edit_review(user, request.data)
            return Response(status=status.HTTP_200_OK)
        except InvalidInputError as err:
            return Response(data={"data": str(err)}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
    
    def delete(self, request, format=None) -> Response:
        """
        Delete review
        Parameters:
            review_id: int
        """
        try:
            ReviewService.delete_review(request.data)
            return Response(status=status.HTTP_200_OK)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None) -> Response:
        """
        Get user details
        Parameters:
            N/A
        """
        data: dict[str, Any] = {}
        
        user = User.objects.get(username=request.user)
        # data["user"] = UserSerializer(user).data
        data["user"] = ProfileUserSerializer(user).data

        return Response(data, status=status.HTTP_200_OK)

    # TODO docstring
    def post(self, request, format=None) -> Response:
            user = User.objects.get(username=request.user)
            data = json.loads(request.body.decode("utf-8"))

            try:
                UserService.update_user(user, data)
            except PasswordsDontMatchError as err:
                return Response(data={"data": str(err)}, status=status.HTTP_406_NOT_ACCEPTABLE)
            
            return Response(status=status.HTTP_200_OK)

