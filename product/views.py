from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcome (request):

    product =[
        {
            'name': 'pump',
            'desc' : 'pumping tool'
        },
        {
            'name': 'solar panel',
            'desc' : 'solar energy'
        },
        {
            'name': 'batteries panel',
            'desc' : 'invventers energy'
        }
    ]
    return render(request, 'product/product.html', {
        'product' : product
    })