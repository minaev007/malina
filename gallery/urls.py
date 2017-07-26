from django.conf.urls import url
from . import views

app_name='gallery'
urlpatterns = [
    url(r'^$', views.gallery_page, name='gallery_page'),
    url(r'^man$', views.man_hairstyle, name='man_hairstyle'),
    url(r'^woman$', views.woman_hairstyle, name='woman_hairstyle'),
    url(r'^nails$', views.nails, name='nails'),    url(r'^nails$', views.nails, name='nails'),    
    url(r'^coloring$', views.coloring, name='coloring'),    
    url(r'^eyelashes$', views.eyelashes, name='eyelashes'),    
    url(r'^eyebrows$', views.eyebrows, name='eyebrows'),    
    url(r'^atmosphere$', views.atmosphere, name='atmosphere'),    
    url(r'^(?P<photo_id>[0-9]+)$', views.detail_photo, name='detail_photo'),
    #url(r'^search$', views.search, name='search'),
]