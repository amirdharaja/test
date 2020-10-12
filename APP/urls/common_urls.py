from django.urls import path
from rest_framework.routers import DefaultRouter

from APP.viewsets import (
    TestViewSet,
)
from APP.views.common_view import (
    Home,
)

router = DefaultRouter()

urlpatterns = (
    path('test/', Home.as_view()),
)