from django.contrib import admin
from . models import Hotel
# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published',
                    'description', 'list_date', 'agent')
    list_display_links = ('id', 'title')
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 10


admin.site.register(Hotel, HotelAdmin)
