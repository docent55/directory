from rest_framework import serializers

from .models import UserProfile


class GetUserProfileSerializer(serializers.ModelSerializer):
    '''info for userProfile'''
    class Meta:
        model = UserProfile
        exclude = ('password',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser')

class GetUserProfilePublicSerializer(serializers.ModelSerializer):
    '''info for userProfile public '''
    class Meta:
        model = UserProfile
        exclude = ('password',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser',
                   'email',
                   'user_permissions',
                   'groups',
                   'phone_number')