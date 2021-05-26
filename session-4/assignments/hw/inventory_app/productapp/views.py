from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from productapp.models import Product


# FUNCTION BASED VIEWS
# (UPDATING TO) generic class based views
# def index(request):
#     return HttpResponse('Welcome Home')

# def catalog(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'productapp/catalog.html', context)

# def catalog_detail(request, id):
#     product = Product.objects.get(pk=id)
#     context = {'product': product}
#     return render(request, 'productapp/catalog_detail.html', context)

    

# Base Class View
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome Home to Class Views!')


# Generic Class View
class ProductListView(ListView):
    model = Product
    # paginate_by = 2
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_list'] = Product.objects.all()
        return context
