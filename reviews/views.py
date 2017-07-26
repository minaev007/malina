from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Review
from django.core.mail import send_mail
from malina import settings

# Create your views here.

def reviews_page(request):
    reviews = Review.objects.filter().all().order_by('-date')
    return render(request, 'reviews/reviews_page.html', 
    {'reviews':reviews})

def create_review(request):
    admin_only = ['Администратор', 'Админ', 'Модератор', 'Administrator', 'Admin', 'Moderator' ]
    errors = []
    reviews = Review.objects.filter().all().order_by('-date')
    if 'name' not in request.POST or 'the_review'  not in request.POST:
         return render(request, 'reviews/reviews_page.html', {'reviews':reviews})
    name = request.POST['name']
    the_review = request.POST['the_review']
    if len(name) < 1 or name.startswith(' '):
        errors.append('Введите имя')
    if len(the_review) < 1 or the_review.startswith(' '):
        errors.append('Введите отзыв')
    if name in admin_only:
         errors.append('Использование данного имени невозможно')
    if errors:
        return render(request, 'reviews/reviews_page.html', {'errors': errors, 'reviews':reviews})
    new_review = Review(name=request.POST['name'], the_review=request.POST['the_review'], date=timezone.now())
    new_review.save()
    send_mail(
        'Появился новый отзыв!',
        the_review,
        settings.EMAIL_HOST_USER,
        ['Mirra826@gmail.com', 'Ali.rohta@gmail.com', 'yurij.zusik@gmail.com'],
        fail_silently=False
    )
    return HttpResponseRedirect(reverse('reviews:thanks'))

def thanks(request):
    return render(request, 'reviews/thanks.html')