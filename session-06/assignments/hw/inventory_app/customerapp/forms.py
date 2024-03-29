from django.forms import ModelForm
from productapp.models import Product

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from customerapp.models import Customer

from django import forms

# class CustomerForm(forms.ModelForm):
#     model = Customer
#
#     class Meta:
#         fields = ['username', 'email', 'password', 'github']

class NewCustomerForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    github = forms.URLField()

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = Customer.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Customer.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def clean_github(self):
        github = self.cleaned_data['github'].lower()
        return github

    def save(self, commit=True):
        # user = User.objects.create_user(
        customer = Customer.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            # self.cleaned_data['github']
        )
        return customer
