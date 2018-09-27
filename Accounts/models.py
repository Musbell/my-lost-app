from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)
# Create your models here.
# class UserProfile(AbstractUser):
#     user = models.OneToOneField(User, on_delete='Cascade', primary_key=True)
#     state = models.CharField(max_length=100)
#     local_government = models.CharField(max_length=100)
#     nationality = models.CharField(max_length=50, null=True)
#     occupation = models.CharField(max_length=50, null=True)
#     gender = models.CharField(max_length=10, choices=GENDER, null=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     address = models.CharField(max_length=100)
#     image = models.ImageField(null=True, upload_to="user_image")
#     phone = models.IntegerField(default=0)
#
#
# @receiver(post_save, sender=User)
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#         post_save.connect(create_profile, sender=User)


# class UserProfileModel(AbstractUser):
#     # user = models.OneToOneField(User, on_delete='Cascade', primary_key=True)
#     state = models.CharField(max_length=100)
#     local_government = models.CharField(max_length=100)
#     nationality = models.CharField(max_length=50, null=True)
#     occupation = models.CharField(max_length=50, null=True)
#     gender = models.CharField(max_length=10, choices=GENDER, null=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     address = models.CharField(max_length=100)
#     image = models.ImageField(null=True, upload_to="user_image")
#     phone = models.IntegerField(default=0)