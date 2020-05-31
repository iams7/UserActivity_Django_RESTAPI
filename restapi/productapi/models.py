from django.db import models
from django.contrib.sessions.backends.db import SessionStore
import pytz

# Create your models here.

class Product (models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    id = models.CharField(max_length=100, primary_key=True)
    real_name= models.CharField(max_length=500)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    activity_periods = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id