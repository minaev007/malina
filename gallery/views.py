from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Photo

# Create your views here.

def gallery_page(request):
    return render(request, 'gallery/gallery_page.html')

def detail_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'gallery/detail_photo.html', {'photo':photo})

'''

def search(request):
    photos = []
    search_list = request.GET['search'].split(' ')
    for word in search_list:
        results = Photo.objects.filter(name__icontains=word)
        for result in results:
            if result not in photos:
                photos.append(result)
    return render(request, 'gallery/search_results.html', {'photos': photos})

    <div class="search">
        <div class="search-say">
            <p>
                <i class="fa fa-search" aria-hidden="true"></i>     Найдите то, что вам нужно!
            </p> 
        </div>
        <div class="search-form">
            <form action="{% url 'gallery:search' %}" method="get">
                <input type="text" maxlength="50" placeholder="Начните вводить тип прически" />
                <input type="submit" value="Поиск"> 
            </form>
        </div>
    </div>
'''

def man_hairstyle(request):
    photos = Photo.objects.filter(path__startswith='gallery/man')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})

def woman_hairstyle(request):
    photos = Photo.objects.filter(path__startswith='gallery/woman')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})

def nails(request):
    photos = Photo.objects.filter(path__startswith='gallery/nails')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})

def coloring(request):
    photos = Photo.objects.filter(path__startswith='gallery/coloring')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})

def eyelashes(request):
    photos = Photo.objects.filter(path__startswith='gallery/eyelashes')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})

def eyebrows(request):
    photos = Photo.objects.filter(path__startswith='gallery/eyebrows')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})

def atmosphere(request):
    photos = Photo.objects.filter(path__startswith='gallery/atmosphere')
    return render(request, 'gallery/hairstyles.html', {'photos':photos})