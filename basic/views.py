from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Services

# Create your views here.

def main_page(request):
    first_slide = Services.objects.filter(category='Парикмахерские услуги')
    second_slide = Services.objects.filter(category='Маникюрные услуги')
    third_slide = Services.objects.filter(category='Косметология')
    forth_slide = Services.objects.filter(category='Услуги массажа')
    return render(request, 'basic/main_page.html', {'first_slide': first_slide, 'second_slide': second_slide, 'third_slide': third_slide, 'forth_slide': forth_slide})
