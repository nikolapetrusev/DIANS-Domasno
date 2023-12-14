from typing import Any

from django.contrib.auth.models import User

from app.models import Review
from app.serializers import ReviewSerializer
from profiles.exceptions import InvalidInputError


class ReviewService:
    @staticmethod
    def create_review(user: User, data: dict[str, Any]) -> None:
        review = Review.objects.create(
            user=user,
            rating=data["rating"],
            comment=comm if (comm := data.get("comment", None)) else None,
            winery_id=data["winery_id"],
        )
        review.save()

    @staticmethod
    def edit_review(user: User, data: dict[str, Any]) -> None:
        review = Review.objects.get(pk=data["review_id"])
        serializer = ReviewSerializer(review, data=data)

        if serializer.is_valid() and review.user == user:
            serializer.save(user=user)
        else:
            raise InvalidInputError("ReviewService.edit_review()")
        
    @staticmethod
    def delete_review(data: dict[str, Any]) -> None:
        review = Review.objects.get(pk=data["review_id"])
        review.delete()
            
