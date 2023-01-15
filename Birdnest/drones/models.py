from django.db import models

# Create your models here.
class PilotTable(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=100)