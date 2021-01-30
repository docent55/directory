from rest_framework import serializers

from .models import UserProfile


class GetUserProfileSerializer(serializers.ModelSerializer):
    '''info for userProfile'''
    class Meta:
        model = UserProfile
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser')