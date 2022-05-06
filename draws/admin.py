from django.contrib import admin

from draws.models import Number, Count


class NumberAdmin(admin.ModelAdmin):
    readonly_fields = [
        'drwNo',
        'drwNoDate',
        'totSellamnt',
        'firstWinamnt',
        'firstPrzwnerCo',
        'drwtNo1',
        'drwtNo2',
        'drwtNo3',
        'drwtNo4',
        'drwtNo5',
        'drwtNo6',
        'bnusNo', ]


class CountAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'cnt', 'bns']


admin.site.register(Number, NumberAdmin)
admin.site.register(Count, CountAdmin)
