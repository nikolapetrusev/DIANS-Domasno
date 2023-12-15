from django.contrib import admin
from django.contrib.auth.models import User

from .extended_user_admin import ExtendedUserAdmin, UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
