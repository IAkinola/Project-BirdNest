from django.db import models

# Create your models here.
class PilotTable(models.Model):
    ndz_time = models.DateTimeField('Time NDZ Breached')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    closest_distance = models.FloatField()
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    
    