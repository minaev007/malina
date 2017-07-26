from django.shortcuts import render
from django.http import HttpResponse
from .models import Promotion
# Create your views here.

def promotion_page(request):
    promotions = []
    promotions_sort = Promotion.objects.all().order_by('-date_end')
    for promotion in promotions_sort:
        if promotion.is_active():
            promotion.listing_advantages()
            promotion.short_date()
            promotions.append(promotion)
        else:
            promotion.delete()
    return render(request, 'promotion/promotion_page.html', {'promotions':promotions})