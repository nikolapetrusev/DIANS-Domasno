from django.urls import path
from . import views

urlpatterns = [
    path("upsert", views.upsert_view, name="app-upsert"),
    path("cities", views.CitiesView.as_view(), name="app-get-all-cities"),
    path("wineries", views.WineriesView.as_view(), name="app-wineries"),
]
