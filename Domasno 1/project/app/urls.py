from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="app-homescreen"),
    path("upsert", views.upsert_view, name="app-upsert"),
]
