from django.contrib import admin
from django.urls import path, include, re_path

from . import views
from productapp.views import IndexView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from productapp.views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

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
    path('catalog/<pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('catalog/<pk>/delete', ProductDeleteView.as_view(), name='product-delete'),

    # catalog/category/ --> ERROR is looking for id
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/new', CategoryCreateView.as_view(), name='new-category'),

    path('category/<pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('category/<pk>/update', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),


    # path('category/<slug>', CategoryDetailView.as_view(), name='category-detail'),
    # path('category/<slug>/update', CategoryUpdateView.as_view(), name='category-update'),
    # path('category/<slug>/delete', CategoryDeleteView.as_view(), name='category-delete'),


    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),

    # path('accounts/profile/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),

    re_path(r'^register/$', views.register, name='register'),
]
