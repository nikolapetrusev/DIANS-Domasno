from app.models import Winery

# TODO dali treba tuka da e order_ by ili u service (so lambda ke treba u service)
class WineryRepository:
    def get_winery_by_id(winery_id: int) -> Winery | None:
        if winery := Winery.objects.get(pk=winery_id):
            return winery

    def get_wineries_by_city(city_id: int) -> list[Winery] | None:
        if wineries := Winery.objects.filter(city__pk=city_id).order_by("name"):
            return wineries

    def get_all_wineries() -> list[Winery] | None:
        if wineries := Winery.objects.order_by("name"):
            return wineries
