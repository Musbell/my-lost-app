from django.db import models

# Create your models here.
class Blog(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=205)
    image = models.ImageField(null=True, upload_to="blog_image")
    content = models.TextField()


    def __str__(self):
        return self.title



class SubscribeMail(models.Model):
    email = models.EmailField(max_length=100)