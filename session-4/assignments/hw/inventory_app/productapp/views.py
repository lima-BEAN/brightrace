from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from productapp.models import Product

from .forms import ProductForm

from django.views.generic.edit import CreateView




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

# def create_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         print(form)
#         print(form.is_valid()) # why is FORM NOT VALID ?? it’s meaningless to validate a form with no data, f.is_valid() --> false
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.save()
#             return render(request, 'productapp/create_product.html', {'form':form})
#         # else:
#         #     form = ProductForm()
#         #     return render(request, 'productapp/create_product.html', {'form': form})
#
#     else:
#         form = ProductForm()
#         return render(request, 'productapp/create_product.html', {'form': form})


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

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'photo']
