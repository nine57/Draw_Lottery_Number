from django.contrib import admin

from draws.models import Number, Count


class NumberAdmin(admin.ModelAdmin):
    pass


class CountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Number)
admin.site.register(Count)
