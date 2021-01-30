from rest_framework.generics import RetrieveAPIView
from .serializers import GetUserProfileSerializer

from .models import UserProfile

class GetUserProfileView(RetrieveAPIView):
    '''UserProfile'''
    queryset = UserProfile.objects.all()
    serializer_class = GetUserProfileSerializer