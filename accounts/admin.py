from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AccoutUser


class AccountUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Extra', {
                'fields': ('avatar', 'phone')
            }
        ),
    )


admin.site.register(AccoutUser, AccountUserAdmin)
