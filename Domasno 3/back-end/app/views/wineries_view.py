from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app.services import WineryService
from app.exceptions import WineryNotFoundError


class WineriesView(APIView):
    def get(self, request, format=None) -> Response:
        """
        Returns wineries by parameter. Only one parameter can be active at a time.
        If no parameters are specified, returns all wineries.

        Parameters:
            winery_id: int | None
            city_id: int | None
        Returns:
            dict[str, Winery] | dict[str, list[Winery]]
        """
        try:
            return Response(
                WineryService.get_wineries(request.GET), status=status.HTTP_200_OK
            )
        except WineryNotFoundError as err:
            return Response(data={"data": str(err)}, status=status.HTTP_404_NOT_FOUND)
