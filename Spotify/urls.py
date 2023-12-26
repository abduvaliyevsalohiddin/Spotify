from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from asosiy.views import *

router = DefaultRouter()
router.register("album", AlbomModelViewSet)
router.register("spooner", QoshiqchiModelViewSet)
router.register("music", QoshiqModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="25-12-2023 vazifa uchun yozilgan Spotify API",
        default_version="V1",
        description="Vazifaga",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqlar/', QoshiqlarAPi.as_view()),
    path('qoshiqchilar/', QoshiqchilarAPi.as_view()),
    path('qoshiqchi/<int:pk>/', QoshiqchiAPi.as_view()),

    path("", include(router.urls)),

    path('docs/',schema_view.with_ui('swagger',cache_timeout=0)),
    # path('docs2/',schema_view.with_ui('redoc',cache_timeout=0)),
]
