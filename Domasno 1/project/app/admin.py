from django.contrib import admin
from .models import City, Winery


class CityAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class WineryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(City, CityAdmin)
admin.site.register(Winery, WineryAdmin)
