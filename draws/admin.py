from django.contrib import admin

from draws.models import Number, Count


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    def numbers(self, obj):
        return [obj.drwtNo1, obj.drwtNo2, obj.drwtNo3, obj.drwtNo4, obj.drwtNo5, obj.drwtNo6, ]

    ordering = ('drwNo',)
    fieldsets = [
        (None, {'fields': ['drwNoDate']}),
        ('Numbers', {
            'fields': [
                'drwtNo1',
                'drwtNo2',
                'drwtNo3',
                'drwtNo4',
                'drwtNo5',
                'drwtNo6',
                'bnusNo',
            ]
        }),
        ('Draw Info', {
            'fields': [
                'totSellamnt',
                'firstWinamnt',
                'firstPrzwnerCo',
            ]
        })
    ]

    list_display = ['drwNo', 'numbers', 'bnusNo']
    # list_display = [
    #     'drwNo',
    #     'drwtNo1',
    #     'drwtNo2',
    #     'drwtNo3',
    #     'drwtNo4',
    #     'drwtNo5',
    #     'drwtNo6',
    #     'bnusNo', ]

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


@admin.register(Count)
class CountAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_diplay = ['id', 'cnt', 'bns']
    readonly_fields = ['id', 'cnt', 'bns']
