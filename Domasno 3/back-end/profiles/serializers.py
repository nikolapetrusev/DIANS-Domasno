from django.contrib.auth.models import User

from rest_framework import serializers
from app.models import Review, Winery


class ProfileWinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = [
            "id",
            "name",
            "city",
            "address",
            "phone",
            "work",
            "coords",
            "rating",
        ]


class ProfileReviewSerializer(serializers.ModelSerializer):
    winery = ProfileWinerySerializer(required=True)
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "rating",
            "comment",
            "winery",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class ProfileUserSerializer(serializers.ModelSerializer):
    reviews = ProfileReviewSerializer(required=True, many=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "reviews",
        ]
