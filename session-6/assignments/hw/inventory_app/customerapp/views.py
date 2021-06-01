from django.views import View
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect

from customerapp.models import Customer

from .forms import NewCustomerForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Customer IndexView')

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    # fields = ['username', 'email', 'password', 'github'] # LEAKS DATA FOR PASSWORD IN DB
    template_name = 'registration/new_customer.html'
    success_url = reverse_lazy('customerapp:customers')
    login_url = '/login/'


    # @login_required --> What if non-user; how to initially register
    def new_customer(request):
        if request.method == 'POST':
            f = NewCustomerForm(request.POST)
            if f.is_valid():
                f.save()
                messages.success(request, 'Account created successfully')
                return HttpResponseRedirect(reverse_lazy('customerapp:login'))
            else:
                return HttpResponse('Form not valid')
        else:
            f = NewCustomerForm()
        return render(request, 'registration/new_customer.html', {'form': f})



# class LoginView(View):
#     login_url = '/login/'
#     redirect_field_name = 'index'


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['customers'] = Customer.objects.all()
        context['customer_list'] = Customer.objects.all()

        return context


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['username', 'email', 'password', 'github']
    template_name = 'customerapp/customer_update.html'
    success_url = reverse_lazy('customerapp:customers')
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # context['customers'] = Customer.objects.all()
        context['customer_list'] = Customer.objects.all()

        return context

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customerapp:customers')


class LoginView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'index'


class LogoutView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'catalog'


# @login_required
# def new_customer(request):
#     if request.method == 'POST':
#         f = NewCustomerForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return HttpResponseRedirect(reverse_lazy('customerapp:login'))
#         else:
#             return HttpResponse('Form not valid')
#     else:
#         f = NewCustomerForm()
#     return render(request, 'registration/new_customer.html', {'form': f})
