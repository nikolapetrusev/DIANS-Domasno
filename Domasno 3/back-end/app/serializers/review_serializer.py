from rest_framework import serializers

from app.models import Review
from profiles.serializers import UserSerializer


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
            return exclusions + ["user"]
