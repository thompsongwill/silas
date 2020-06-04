from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotels, name='hotels'),
    path('<int:hotel_id>', views.hotel, name='hotel'),
    path('search2/', views.search2, name='search2')
]
