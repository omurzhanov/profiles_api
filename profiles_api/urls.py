from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLoginView


router = DefaultRouter()
router.register('profile', UserViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('', include(router.urls)),
]