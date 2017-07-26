from django.contrib import admin
from .models import Promotion
# Register your models here.

class PromotionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Название', {'fields': ['name']}), 
        ('Описание', {'fields': ['description']}),
        ('Список преимуществ', {'fields': ['list_of_advantages']}),
        ('Заключение', {'fields': ['last_words']}),
        ('Дата начала', {'fields': ['date_start']}),
        ('Дата окончания', {'fields':['date_end']})
    ]
    list_display = ('name', 'description', 'list_of_advantages', 'last_words', 'date_start', 'date_end')
    list_filter = ['date_start']
    search_fields = ['name']

admin.site.register(Promotion, PromotionAdmin)
