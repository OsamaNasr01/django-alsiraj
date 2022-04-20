from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')
    list_filter = ('price',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Product, ProductAdmin)