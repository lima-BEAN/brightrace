from django.shortcuts import render, get_object_or_404

# Create your views here.
from cart.cart import Cart
from shop.models import Product, Category


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None
    return render(request, 'shop/product_list.html', {'product_list': products,
                                                      'category': category,
                                                      'categories': categories,
                                                      'cart': Cart(request)})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    print(product)
    categories = Category.objects.all()
    return render(request, 'shop/product_detail.html', {'product': product,
                                                        'categories': categories,
                                                        'cart': Cart(request)})
