from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse, reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from productapp.models import Product

from .forms import ProductForm

from django.contrib.auth.mixins import LoginRequiredMixin


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
        # return HttpResponse('Welcome Home to Class Views!')
        return render(request, 'productapp/index.html')


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
    template_name = 'productapp/create_product.html'
    success_url = reverse_lazy('productapp:catalog')
    # login_url = 'login'# appname:viewname accounts/login

    # def form_valid(self, form): #MRO
    #     # form.instance.user = self.request.user # logged in user
    #     return super(ProductCreate, self).form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'photo']
    template_name = 'productapp/product_update.html'
    success_url = reverse_lazy('productapp:catalog')
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['product_list'] = Product.objects.all()
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('productapp:catalog')


class LoginView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'catalog'

class LogoutView(View):
    # logout_url = '/logout/'
    redirect_field_name = 'catalog'
