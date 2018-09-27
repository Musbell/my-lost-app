from django.db import models

# Create your models here.

STATUS = (
    ('STOLEN', 'STOLEN'),
    ('LOST', 'LOST'),
    ('MISPLACED', 'MISPLACED')
)

STATES = (
    ('ABUJA', 'ABUJA '),
    ('ABIA', 'ABIA'),
    ('ADAMAWA', 'ADAMAWA'),
    ('AKWA IBOM', 'AKWA IBOM'),
    ('ANAMBRA', 'ANAMBRA'),
    ('BAUCHI', 'BAUCHI'),
    ('BAYELSA', 'BAYELSA'),
    ('BENUE', 'BENUE'),
    ('BORNO', 'BORNO'),
    ('CROSS RIVER', 'CROSS RIVER'),
    ('DELTA', 'DELTA'),
    ('EBONYI', 'EBONYI'),
    ('ENUGU', 'ENUGU'),
    ('EDO', 'EDO'),
    ('EKITI', 'EKITI'),
    ('GOMBE', 'GOMBE'),
    ('IMO', 'IMO'),
    ('JIGAWA', 'JIGAWA'),
    ('KADUNA', 'KADUNA'),
    ('KANO', 'KANO'),
    ('KATSINA', 'KATSINA'),
    ('KEBBI', 'KEBBI'),
    ('KOGI', 'KOGI'),
    ('KWARA', 'KWARA'),
    ('LAGOS', 'LAGOS'),
    ('NASARAWA', 'NASARAWA'),
    ('NIGER', 'NIGER'),
    ('OGUN', 'OGUN'),
    ('ONDO', 'ONDO'),
    ('OSUN', 'OSUN'),
    ('OYO', 'OYO'),
    ('PLATEAU', 'PLATEAU'),
    ('RIVERS', 'RIVERS'),
    ('SOKOTO', 'SOKOTO'),
    ('YOBE', 'YOBE'),
    ('ZAMFARA', 'ZAMFARA')
)

class ReportModel(models.Model):
    date = models.DateTimeField(auto_now=True)
    deviceName = models.CharField(max_length=50)
    deviceModel = models.CharField(max_length=50)
    serialNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS, null=True)
    state = models.CharField(max_length=250, choices=STATES, default="")
    email = models.EmailField(blank=True)
    phone = models.CharField(default=0, max_length=15)


    def __str__(self):
        return self.deviceName + '' + self.deviceModel

class FoundModel(models.Model):
    date = models.DateTimeField(auto_now=True)
    deviceName = models.CharField(max_length=50)
    deviceModel = models.CharField(max_length=50)
    serialNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS, null=True)
    state = models.CharField(max_length=250, choices=STATES, default="")
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



class AgentRequest(models.Model):
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=250, choices=STATES, default="")
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(default=0, max_length=15)
    short_bio = models.TextField()


    def __str__(self):
        return self.name


