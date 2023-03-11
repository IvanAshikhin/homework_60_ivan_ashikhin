from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect

from webapp.models import Product

from webapp.forms import ProductForm


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'detail.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'add.html', context={'form': form})
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add.html', context={'form': form})
    else:
        Product.objects.create(**form.cleaned_data)
        return redirect('index_page')


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'update.html', {'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.save()
            return redirect('index_page')
        else:
            return render(request, 'update.html', {'form': form, 'product': product})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'confirm_delete.html', context={"product": product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index_page')
