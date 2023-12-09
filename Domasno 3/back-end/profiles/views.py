import json
from typing import Any

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.models import Winery, Review
from app.serializers import ReviewSerializer, WinerySerializer
from profiles.serializers import UserSerializer


class FavoritesView(APIView):
    permission_classes = (IsAuthenticated,)
 
    def get(self, request, format=None) -> Response:
        """
        Get favorite wineries.
        Parameters:
            N/A
        Returns:
            wineries: list[Winery]
        """
        data: dict[str, Any] = {}

        user = User.objects.get(username=request.user)

        favorites = fav if (fav := user.extended.favorites) else []
        favorites_serialized = WinerySerializer(favorites, many=True)
        data["favorites"] = favorites_serialized.data

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
        w_id = json.loads(request.body.decode("utf-8"))["winery_id"]
        # TODO ako ne postoe vinarija so taj iD?
        user.favorites.add(Winery.objects.get(pk=w_id))

        return Response(status=status.HTTP_202_ACCEPTED)


# TODO dodaj PUT metod za edit na review?
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
        # data = request.POST
        
        review = Review.objects.create(
            user=user,
            rating=data["rating"],
            comment=comm if (comm := data.get("comment", None)) else None,
        )
        winery = Winery.objects.get(pk=data["winery_id"])
        winery.reviews.add(review)

        return Response(status=status.HTTP_201_CREATED)
    
    def put(self, request, format=None) -> Response:
        review = Review.objects.get(pk=request.data["review_id"])
        user = User.objects.get(username=request.user)

        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid() and review.user == user:
            serializer.save(user=user)
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None) -> Response:
        data: dict[str, Any] = {}
        
        user = User.objects.get(username=request.user)
        data["user"] = UserSerializer(user).data

        return Response(data, status=status.HTTP_200_OK)

    # TODO treba PUT ne POST
    # komplicinrano ke e so put zaradi required fields itn..
    def post(self, request, format=None) -> Response:
            user = User.objects.get(username=request.user)

            if tmp := request.POST.get("first_name", None):
                user.first_name = tmp
            
            # if tmp := json.loads(request.body.decode("utf-8")).get("first_name", None):
            #     user.first_name = tmp
            # if tmp := json.loads(request.body.decode("utf-8")).get("first_name", None):
            #     user.last_name = tmp
            # if tmp := json.loads(request.body.decode("utf-8")).get("email", None):
            #     user.email = tmp
            # if tmp := json.loads(request.body.decode("utf-8")).get("username", None):
            #     if User.objects.filter(username=tmp).exists():
            #         return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            #     user.last_name = tmp
            # if tmp := json.loads(request.body.decode("utf-8")).get("password", None):
            #     user.set_password(tmp)

            user.save()
            
            return Response(status=status.HTTP_200_OK)

