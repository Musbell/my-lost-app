from django.db import models

# Create your models here.

STATUS = (
    ('STOLEN', 'STOLEN'),
    ('LOST', 'LOST')
)

class ReportModel(models.Model):
    date = models.DateTimeField(auto_now=True)
    deviceName = models.CharField(max_length=50)
    deviceModel = models.CharField(max_length=50)
    serialNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS, null=True)
    state = models.CharField(max_length=250, default="state")
    email = models.EmailField(blank=True)
    phone = models.CharField(default=0, max_length=15)


    def __str__(self):
        return self.deviceName + '' + self.deviceModel



class Suggestion(models.Model):
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.email



