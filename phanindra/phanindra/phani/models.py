from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
"""


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profiles_pic',blank=True)

    def __str__(self):
        return self.user.username