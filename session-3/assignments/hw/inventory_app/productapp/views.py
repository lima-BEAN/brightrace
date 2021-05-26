from django.shortcuts import render
from django.http import HttpResponse

from productapp.models import Product

def index(request):
    return HttpResponse('Welcome Home')

def catalog(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'productapp/catalog.html', context)

def catalog_detail(request, id):
    product = Product.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'productapp/catalog_detail.html', context)
