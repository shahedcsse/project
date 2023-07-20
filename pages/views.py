from django.shortcuts import render
from django.http import HttpResponse


from listings.models import Listings
from listings.choices import price_choices, bedroom_choices, div_choices
from realtors.models import Realtor


# Create your views here.
def index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'div_choices': div_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
