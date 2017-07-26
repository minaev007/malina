from django.contrib import admin
from .models import Services

# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Категория', {'fields': ['category']}),
        ('Имя', {'fields': ['name']}),
       ('Дата', {'fields':['date']})         
    ]
    list_display = ('category', 'name', 'date')
    list_filter = ['category']

admin.site.register(Services, ServicesAdmin)