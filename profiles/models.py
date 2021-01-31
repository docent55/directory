from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    '''Profiles'''
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    middle_name = models.CharField(max_length=30)
    first_login = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    fieldofactivity = models.ManyToManyField('FieldOfActivity', related_name='user')

class FieldOfActivity(models.Model):
    ''''''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name