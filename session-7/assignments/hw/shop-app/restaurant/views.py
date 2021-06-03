from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView

from restaurant.forms import RestaurantForm, DishForm
from restaurant.models import Restaurant, Dish, RestaurantReview, RATING_CHOICES


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'restaurant/restaurant_detail.html'
    extra_context = {'RATING_CHOICES': RATING_CHOICES}


class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant/restaurant_create.html'
    success_url = reverse_lazy('restaurant:restaurant_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)


class DishCreate(LoginRequiredMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'restaurant/restaurant_create.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DishCreate,self).form_valid(form)


def review_create(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    print(request)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('restaurant:restaurant_detail', args=(restaurant.id,)))