from django.urls import path

from draws.views import NumberView, CountView, SetUpView

urlpatterns = [
    path('', NumberView.as_view()),
    path('/update', CountView.as_view()),
    path('/setup', SetUpView.as_view()),
]
