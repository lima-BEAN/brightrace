from django import forms
from restaurant.models import Restaurant, Dish


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        # fields = '__all__'
        exclude = ('user', 'date')

    def clean(self):
        pass


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        # fields = '__all__'
        exclude = ('user', 'date')

    def clean(self):
        pass