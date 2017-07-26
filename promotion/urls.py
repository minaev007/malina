from django.conf.urls import url
from . import views

app_name = 'promotion'
urlpatterns = [
    url(r'^$', views.promotion_page, name='promotion_page'),
]