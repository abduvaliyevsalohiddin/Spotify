from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from asosiy.views import *

router = DefaultRouter()
router.register("album", AlbomModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqlar/', QoshiqlarAPi.as_view()),
    path('qoshiqchilar/', QoshiqchilarAPi.as_view()),
    path('qoshiqchi/<int:pk>/', QoshiqchiAPi.as_view()),

    path("", include(router.urls)),

]
