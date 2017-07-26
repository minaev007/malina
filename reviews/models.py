from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Review(models.Model):
    name = models.CharField('name', max_length=30)
    the_review = models.CharField('the review', max_length=500)
    date = models.DateTimeField('date published')

    def __str__(self):
        return '{} {}'.format(self.name, self.the_review[:10])
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.date >= now - datetime.timedelta(days=7)