from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer
from .models import User
from .permissions import UpdateOwnProfile


class UserViewSet(ModelViewSet):
    """Handle creating and updating a user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
