from django.contrib import admin
from . models import Shop
# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'size', 'price', 'is_published',
                    'description', 'list_date', 'agent')
    list_display_links = ('id', 'size')
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 10


admin.site.register(Shop, ShopAdmin)
