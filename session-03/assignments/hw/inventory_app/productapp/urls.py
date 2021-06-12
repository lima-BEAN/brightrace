from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'productapp'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.catalog, name='catalog'),
    path('<int:id>', views.catalog_detail, name='catalog-detail'),
]
