from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import ExtendedUser


class ExtendedUserAdmin(admin.StackedInline):
    model = ExtendedUser
    can_delete = False
    verbose_name_plural = "Корисници"
    readonly_fields = ("favorites",)


class UserAdmin(BaseUserAdmin):
    inlines = [ExtendedUserAdmin]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
