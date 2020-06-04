from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Hotel

# Create your views here.


def hotels(request):
    hotels = Hotel.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(hotels, 4)
    page = request.GET.get('page')
    paged_hotels = paginator.get_page(page)

    context = {
        'hotels': paged_hotels
    }

    return render(request, 'hotels/hotels.html', context)


def hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)

    context = {
        'hotel': hotel
    }

    return render(request, 'hotels/hotel.html', context)


def search2(request):

    queryset_list = Hotel.objects.order_by('-list_date')

    # Keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # if 'title' in request.GET:
    #     title = request.GET['title']
    #     if title:
    #         queryset_list = queryset_list.filter(
    #             title__icontains=title)

    context = {
        'hotels': queryset_list,
        'values': request.GET

    }
    return render(request, 'hotels/search2.html', context)
