from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Services(models.Model):
    category = models.CharField('category', max_length=50)
    name = models.CharField('name', max_length=100)
    date = models.DateTimeField('date published')
    
    def __str__(self):
        return '{}'.format(self.name)


