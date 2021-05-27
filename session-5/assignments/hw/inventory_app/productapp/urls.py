from django.contrib import admin
from django.urls import path, include, re_path

from . import views
from productapp.views import IndexView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.contrib.auth import views as auth_views

app_name = 'productapp'

urlpatterns = [

    # UPDATING TO generic class based views
    #
    # path('', views.index, name='index'),
    # path('catalog/', views.catalog, name='catalog'),
    # path('catalog/<int:id>', views.catalog_detail, name='catalog-detail'),
    # path('catalog/create-product', views.create_product, name='create-product'),


    path('', IndexView.as_view(), name='index'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('catalog/<pk>', ProductDetailView.as_view(), name='catalog-detail'),
    path('create-product', ProductCreateView.as_view(), name='create-product'),
    path('catalog/<pk>/product-update', ProductUpdateView.as_view(), name='product-update'),
    path('catalog/<pk>/product-delete', ProductDeleteView.as_view(), name='product-delete'),

    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),


    re_path(r'^register/$', views.register, name='register'),
]
