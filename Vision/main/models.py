from datetime import date
from django.db import models
import datetime

# Create your models here.
class NumberPlate(models.Model): 
    name = models.CharField(max_length=50) 
    plate_image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=datetime.datetime.now) 