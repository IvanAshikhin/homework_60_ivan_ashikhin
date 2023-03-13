from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from webapp.models import Order
from webapp.models.order import OrderItem
from webapp.models import ProductCart
from webapp.forms import OrderForm


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'create_order.html'

    def form_valid(self, form):
        cart_items = ProductCart.objects.all()
        order = form.save()
        for item in cart_items:
            OrderItem.objects.create(
                product=item.product,
                order=order,
                quantity=item.count
            )
        cart_items.delete()
        return redirect('index_page')
