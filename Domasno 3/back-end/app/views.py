import json
from typing import Any

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import City, Winery
from .services.upsert import upsert
from .services.pipelines.cleanup import cleanup_pipeline
from .serializers import CitySerializer, WinerySerializer


# TODO brisi
@require_http_methods(["GET"])
def home(request) -> HttpResponse:
    context = {
        "asd": "nesto tuka",
        "bdc": "dr nesto tuka",
    }

    return render(request, "app/homescreen.html", context)


@staff_member_required()
@require_http_methods(["GET"])
def upsert_view(request) -> HttpResponse:
    """
    Upserts data from json into database.
    Parameters:
        N/A
    Returns:
        HttpResponse
    """
    data = cleanup_pipeline()
    upsert(data)

    response_data = {
        "is_successfull": True,
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# TODO namesto 404 da vrakja samo prazna lista, ne samo tuka tuku i u drugio View
class CitiesView(APIView):
    def get_city_by_id(self, city_id: int, data: dict[str, Any]) -> Response:
        '''
        Returns city by ID
        Parameters:
            city_id: int
        Returns
            City
        '''
        if city := City.objects.get(pk=city_id):
            data["city"] = CitySerializer(city).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get_all_cities(self, data: dict[str, Any]) -> Response:
        """
        Returns all cities.
        Parameters:
            N/A
        Returns:
            list[City]
        """
        cities = obj if (obj := City.objects.filter().all()) else []
        if cities := City.objects.all():
            data["cities"] = CitySerializer(cities, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, format=None) -> Response:
        """
        Returns cities by parameter. If no parameters are specified, returns all wineries.
        Parameters:
            city_id: int
        Returns:
            City | list[City]
        """
        data: dict[str, Any] = {}

        # Return by winery id
        if city_id := request.GET.get("city_id", None):
            return self.get_city_by_id(city_id, data)
        # Return all
        else:
            return self.get_all_cities(data)



class WineriesView(APIView):
    def get_winery_by_id(self, winery_id: int, data: dict[str, Any]) -> Response:
        """
        Returns winery by ID
        Parameters:
            winery_id: int
        Returns:
            Winery
        """
        if winery := Winery.objects.get(pk=winery_id):
            data["winery"] = WinerySerializer(winery).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_wineries_by_city(self, city_id: int, data: dict[str, Any]) -> Response:
        """
        Returns all the wineries in selected city.
        Parameters:
            city_id: int
        Returns:
            list[Winery]
        """
        if wineries := Winery.objects.filter(city__pk=city_id):
            data["wineries"] = WinerySerializer(wineries, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_all_wineries(self, data: dict[str, Any]) -> Response:
        """
        Returns all of the wineries
        Parameters:
            N/A
        Returns:
            list[Winery]
        """
        if wineries := Winery.objects.all():
            wineries_serialized = WinerySerializer(wineries, many=True)
            data["wineries"] = wineries_serialized.data
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, format=None) -> Response:
        """
        Returns wineries by parameter. Only one parameter can be active at a time.
        If no parameters are specified, returns all wineries.
        Parameters:
            winery_id: int
            city_id: int
        Returns:
            Winery | list[Winery]
        """
        data: dict[str, Any] = {}

        # Return by winery id
        if winery_id := request.GET.get("winery_id", None):
            return self.get_winery_by_id(winery_id, data)

        # Return by city id
        elif city_id := request.GET.get("city_id", None):
            return self.get_wineries_by_city(city_id, data)

        # Return all
        else:
            return self.get_all_wineries(data)
