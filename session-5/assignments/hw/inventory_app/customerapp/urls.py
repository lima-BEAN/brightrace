from django.urls import include, path, re_path

from . import views
from customerapp.views import IndexView
from django.contrib.auth import views as auth_views

from customerapp.views import IndexView, CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

app_name = 'customerapp'

urlpatterns = [
    # path('', IndexView.as_view(), name='index'),
    path('', CustomerListView.as_view(), name='customers'),
    # path('new-customer', CustomerCreateView.as_view(), name='new-customer'),
    path('<pk>', CustomerDetailView.as_view(), name='customer-detail'),
    path('<pk>/customer-update', CustomerUpdateView.as_view(), name='customer-update'),
    path('<pk>/customer-delete', CustomerDeleteView.as_view(), name='customer-delete'),

    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),

    # path('accounts/profile/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),

    # re_path(r'^register/$', views.register, name='register'),
    # re_path(r'^register/$', views.register, name='register')

    re_path(r'^new-customer/$', views.new_customer, name='new-customer'),


]
