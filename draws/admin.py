from django.contrib import admin

from .models import Number


class NumberAdmin(admin.ModelAdmin):
    list_display = "__all__"


admin.site.register(Number)
