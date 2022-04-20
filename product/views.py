from django.http import HttpResponse
from django.shortcuts import render

from product.models import Product

# Create your views here.

def welcome (request):

    product = Product.objects.all()
    return render(request, 'product/product.html', {
        'product' : product
    })