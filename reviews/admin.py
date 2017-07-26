from django.contrib import admin
from . models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Имя', {'fields':['name']}),
        ('Отзыв', {'fields':['the_review']}),
        ('Дата', {'fields':['date']}) 
    ]
    list_display = ('name', 'the_review', 'date')
    list_filter = ['date']
    search_fields = ['name']

admin.site.register(Review, ReviewAdmin)