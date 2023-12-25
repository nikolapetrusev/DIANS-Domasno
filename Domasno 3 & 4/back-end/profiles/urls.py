from django.urls import path

from . import views


urlpatterns = [
    path("favorites/", views.FavoritesView.as_view(), name="profiles-favorites"),
    path("visited/", views.VisitedView.as_view(), name="profiles-visited"),
    path("reviews/", views.ReviewsView.as_view(), name="profiles-reviews"),
    path("profile/", views.ProfileView.as_view(), name="profiles-profile"),
]
