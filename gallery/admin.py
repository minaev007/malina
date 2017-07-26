from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Имя', {'fields':['name']}),
        ('Путь к изображению', {'fields':['path']}),
        ('Дата', {'fields':['date']}) 
    ]
    list_display = ('name', 'path', 'date')
    list_filter = ['date']
    search_fields = ['name']

admin.site.register(Photo, PhotoAdmin)