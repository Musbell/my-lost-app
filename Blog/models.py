from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=205)
    image = models.ImageField(null=True, upload_to="blog_image")
    content = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})



#class SubscribeMail(models.Model):
 #   name = models.CharField(max_length=100, default="guest")
  #  email = models.EmailField(max_length=100)


#
#class Comments(models.Model):
 #   name = models.CharField(max_length=50)
 #   image = models.ImageField(null=True, upload_to="comment_image", blank=True)
  #  email = models.EmailField(max_length=100)
 #   comment = models.TextField()
