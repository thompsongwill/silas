from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Shop

# Create your views here.


def shops(request):
    shops = Shop.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(shops, 4)
    page = request.GET.get('page')
    paged_shops = paginator.get_page(page)

    context = {
        'shops': paged_shops
    }

    return render(request, 'shops/shops.html', context)


def shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)

    context = {
        'shop': shop
    }

    return render(request, 'shops/shop.html', context)
