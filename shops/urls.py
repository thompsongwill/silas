from django.urls import path
from . import views

urlpatterns = [
    path('', views.shops, name='shops'),
    path('<int:shop_id>', views.shop, name='shop')
]
