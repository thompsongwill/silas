from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.choice import price_choices, bedroom_choices, property_type
from .models import Listing

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(
                title__icontains=title)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__iexact=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {

        'bedroom_choice': bedroom_choices,
        'price_choice': price_choices,
        'property_type': property_type,
        'listings': queryset_list,
        'values': request.GET

    }
    return render(request, 'listings/search.html', context)
