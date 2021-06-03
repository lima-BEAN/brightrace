from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy

from cart.cart import Cart
from shop.models import Product


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_add(request, product_id):
    session_cart_obj = Cart(request)
    session_cart_obj.addnew(get_object_or_404(Product, id=product_id))
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    session_cart_obj = Cart(request)
    session_cart_obj.removeone(product_id)
    return HttpResponseRedirect(reverse_lazy('cart:cart_detail'))