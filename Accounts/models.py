from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import sys


sys.setrecursionlimit(1500)

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    state = models.CharField(max_length=50)
    local_government = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=150)
    image = models.ImageField(null=True, upload_to="user_image")
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
   # if created:
        #Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
 #   instance.profile.save()



@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
     if kwargs['created']:
         user_profile = UserProfile.objects.create(user=kwargs['instance'])
         post_save.connect(create_profile, sender=User)
