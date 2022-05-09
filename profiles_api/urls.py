from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLoginView, ProfileFeedViewSet


router = DefaultRouter()
router.register('profile', UserViewSet)
router.register('feed', ProfileFeedViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('', include(router.urls)),
]