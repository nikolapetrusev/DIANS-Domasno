from rest_framework import serializers

from profiles.serializers import UserSerializer
from .models import City, Review, Winery, Coords


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "id",
            "name",
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            "longitude",
            "latitude",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "rating",
            "comment",
        ]
        
        def get_validation_exclusions(self):
            exclusions = super(ReviewSerializer, self).get_validation_exclusions()
            return exclusions + ['user']


class WinerySerializer(serializers.ModelSerializer):
    city = CitySerializer(required=True)
    coords = CoordsSerializer(required=True)
    reviews = ReviewSerializer(required=True, many=True)

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
            "reviews",
        ]
