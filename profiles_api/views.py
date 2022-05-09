from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, ProfileFeedItemSerializer
from .models import User, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnStatus


class UserViewSet(ModelViewSet):
    """Handle creating and updating a user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedViewSet(ModelViewSet):
    """Handles CRUD on feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    permission_classes = (UpdateOwnStatus, IsAuthenticated,)
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
