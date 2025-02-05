#------------------------- Why No Models uselde for User --------------#
"""Here we uses Django's built-in User model we don't need to define a
custom model in models.py for this implementation of user registration.
 if you're doing something more complex with additional fields,
 you would create a custom model in models.py"""


# from django.db import models
#
#
# # Create your models here.
#
# class UserProfile(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255, blank=True)
#     last_name = models.CharField(max_length=255, blank=True)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#
#
# def __str__(self):
#     return self.username

