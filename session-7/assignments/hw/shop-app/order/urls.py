from django.urls import re_path

from order import views

app_name = 'order'
urlpatterns = [
    re_path(r'^create/', views.order_create, name='order_create'),
    re_path(r'^cancel/', views.OrderCancel.as_view(), name='order_cancel'),
    re_path(r'^pdf/', views.order_pdf, name='order_pdf'),

]