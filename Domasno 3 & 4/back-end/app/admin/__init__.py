from django.contrib import admin

from app.models import City, Review, Winery

from .city_admin import CityAdmin
from .review_admin import ReviewAdmin
from .winery_admin import WineryAdmin

admin.site.register(City, CityAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Winery, WineryAdmin)
