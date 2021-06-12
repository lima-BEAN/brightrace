from django.urls import re_path
from django.utils import timezone
from django.views.generic import ListView, UpdateView, DetailView

from restaurant import views
from restaurant.forms import RestaurantForm, DishForm
from restaurant.models import Restaurant, Dish
from restaurant.views import RestaurantDetail, RestaurantCreate, DishCreate

app_name = 'restaurant'
urlpatterns = [
    # List latest 5 restaurants, ex.: /restaurants/
    re_path(r'^$',
            ListView.as_view(
                # model = Restaurant,
                queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
                context_object_name='latest_restaurant_list',
                template_name=' restaurant/restaurant_list.html'),
            name='restaurant_list'),

    # Restaurant details, ex.: /restaurants/1/
    re_path(r'^(?P<pk>\d+)/$',
            RestaurantDetail.as_view(),
            name='restaurant_detail'),

    # Create a restaurant, ex.: /restaurants/create/
    re_path(r'^create/$',
            RestaurantCreate.as_view(),
            name='restaurant_create'),

    # Update restaurant details, ex.: /restaurants/1/update/
    re_path(r'^(?P<pk>\d+)/update/$',
            UpdateView.as_view(
                model=Restaurant,
                template_name='restaurant/restaurant_update.html',
                form_class=RestaurantForm),
            name='restaurant_update'),

    # Restaurant dish details, ex: /restaurants/1/dishes/1/
    re_path(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Dish,
                template_name='restaurant/dish_detail.html'),
            name='dish_detail'),

    # Create a restaurant dish, ex.: /restaurants/1/dishes/create/
    re_path(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
            DishCreate.as_view(),
            name='dish_create'),

    # Update restaurant dish details, ex.: /restaurants/1/dishes/1/edit/
    re_path(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
            UpdateView.as_view(
                model=Dish,
                template_name='restaurant/restaurant_update.html',
                form_class=DishForm),
            name='dish_update'),

    # Create a restaurant review, ex.: /restaurants/1/reviews/create/
    re_path(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
            views.review_create,
            name='review_create'),
]
