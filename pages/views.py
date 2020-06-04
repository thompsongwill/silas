from django.shortcuts import render
from listings.choice import price_choices, bedroom_choices, property_type

from listings.models import Listing
# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_choice': bedroom_choices,
        'price_choice': price_choices,
        'property_type': property_type

    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
