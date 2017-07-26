from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Photo(models.Model):
    path = models.CharField('path', max_length=100, default='Empty')
    name = models.CharField('name', max_length=50)
    date = models.DateTimeField('date')

    def __str__(self):
        return '{}.'.format(self.path)
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.date >= now - datetime.timedelta(days=7)