from django.urls import path

from draws.views import NumberView, CountView

urlpatterns = [
    path('', NumberView.as_view()),
    path('/update', CountView.as_view()),
]
