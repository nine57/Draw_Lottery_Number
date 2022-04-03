from django.urls import path
from draws.views import DrawNumberView
# , StatisticsView

urlpatterns = [
    path('', DrawNumberView.as_view()),
    # path('/patch', StatisticsView.as_view()),
]
