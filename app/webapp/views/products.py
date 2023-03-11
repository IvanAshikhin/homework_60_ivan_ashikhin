from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductForm


class ProductDetail(DetailView):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'


class TaskAddView(CreateView):
    template_name = 'add.html'
    model = Product
    context_object_name = 'product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    context_object_name = 'product'
    model = Product
    success_url = reverse_lazy('index_page')
