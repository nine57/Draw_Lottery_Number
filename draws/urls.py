from django.urls import path
from draws.views import DrawNumberView, GetNumberView

urlpatterns = [
    path('', DrawNumberView.as_view()),
    path('/update', GetNumberView.as_view()),
]
