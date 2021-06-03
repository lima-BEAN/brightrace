import io

from django.core.mail import EmailMessage
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, RedirectView
from reportlab.pdfgen import canvas

from cart.cart import Cart
from order.forms import OrderForm
from order.models import Order, Order_Detail
from shop.models import Product


def order_create(request):
    cart = Cart(request)
    print(cart)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_obj = form.save()
            for item in cart:
                product = item['product']
                product_obj = get_object_or_404(Product, name=product.name, slug=product.slug)
                quantity = item['quantity']
                price = item['price']
                Order_Detail.objects.create(order=order_obj,
                                            product=product_obj,
                                            quantity=quantity,
                                            price=price)
        cart.clear() # Clear the cart dictionary object
        request.session['OrderId'] = order_obj.pk

        return render(request, 'order/success.html')
    else:
        form = OrderForm()
        return render(request, 'order/order_create.html', {'form': form, 'cart': cart})


def order_pdf(request):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    order_id = int(request.session['OrderId'])
    text = str(Order.objects.get(pk=order_id))
    pdf.drawString(100,100,text)
    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    # code to send the mail
    email = EmailMessage(
        'Order Received', #Subject
        'This is email Message in plain text', #body
        'kanchan.rade@gmail.com', #From Address
        ['kanchan.patil@summitworks.com'] #To Address
    )
    email.attach('order.pdf',buffer.read())
    email.send()

    return FileResponse(buffer,as_attachment=True,filename='order.pdf')

class OrderCancel(RedirectView):
    pass

