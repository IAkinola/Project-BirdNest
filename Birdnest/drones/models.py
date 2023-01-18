from django.db import models

# Create your models here.
class PilotTable(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    closest_distance = models.IntegerField()
    ndz_time = models.DateTimeField('Time NDZ Breached')