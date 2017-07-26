from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Promotion(models.Model):
    name = models.CharField('name', max_length=100)
    description = models.CharField('description', blank=True, max_length=1000)
    list_of_advantages = models.CharField('list of advantages', blank=True, max_length=1000)
    last_words = models.CharField('last words', blank=True, max_length=500)
    date_start = models.DateTimeField('date start')
    date_end = models.DateTimeField('date end')

    def __str__(self):
        return self.name

    def is_active(self):
        return self.date_end > timezone.now()

    def listing_advantages(self):
        self.list_of_advantages = self.list_of_advantages.split(', ')            

    def short_date(self):
        self.date_start = str(self.date_start).split(' ')[0]
        self.date_end = str(self.date_end).split(' ')[0]