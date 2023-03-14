from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from webapp.models import Product, ProductCart


class MaxCountValidator:
    def __init__(self, message=None):
        self.message = message or 'The quantity of the product exceeds the quantity in stock.'

    def __call__(self, value):
        if value > self.product.remain:
            raise ValidationError(self.message)


class AddToCartView(CreateView):
    model = ProductCart
    template_name = 'add_to_cart.html'
    fields = ['count']
    validator = MaxCountValidator()

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        if product.remain == 0:
            return redirect('index_page')
        if form.cleaned_data['count'] > product.remain:
            self.validator.product = product
            form.add_error('count', self.validator.message)
            return self.form_invalid(form)
        product_cart, created = ProductCart.objects.get_or_create(product=product, defaults={'count': 0})
        if not created and product_cart.count >= product.remain:
            return redirect('index_page')
        product_cart.count += form.cleaned_data['count']
        product_cart.save()
        return redirect('index_page')

    def get_success_url(self):
        return reverse_lazy('index_page')


class CartView(ListView):
    model = ProductCart
    template_name = 'cart.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_cost = sum([product.product.cost * product.count for product in context['object_list']])
        context['total_cost'] = total_cost
        return context


class DeleteCartView(DeleteView):
    model = ProductCart
    success_url = reverse_lazy('cart')
    template_name = 'remove_from_cart.html'
