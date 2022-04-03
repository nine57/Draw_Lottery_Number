from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Draw_Lottery_Number",
        default_version='v1',
        description="Lotto 번호",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # django 앱
    path('draws', include('draws.urls')),
    path('admin', admin.site.urls),

    # swagger setting
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]
