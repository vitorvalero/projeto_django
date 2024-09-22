from django.contrib import admin
from store.models import Coffee


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'quantity', 'farm',
                    'region', 'profile', 'roast', 'price')
    search_fields = ('name', 'type', 'quantity', 'farm',
                     'region' 'profile', 'roast')
    

admin.site.register(Coffee, StoreAdmin)
