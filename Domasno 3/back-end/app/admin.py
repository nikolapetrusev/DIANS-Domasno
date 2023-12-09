from django.contrib import admin
from .models import City, Review, Winery


class CityAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class WineryAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class ReviewAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(City, CityAdmin)
admin.site.register(Winery, WineryAdmin)
admin.site.register(Review, ReviewAdmin)
