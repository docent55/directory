from rest_framework.generics import RetrieveAPIView
from .serializers import GetUserProfileSerializer, GetUserProfilePublicSerializer

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile

class UserProfilePublicView(ModelViewSet):
    '''User profile public'''
    queryset = UserProfile.objects.all()
    serializer_class = GetUserProfilePublicSerializer
    permissions = [permissions.AllowAny]

class UserProfileView(ModelViewSet):
    '''User profile'''
    serializer_class = GetUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)