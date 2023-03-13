from django import forms
from webapp.models import Product
from webapp.models import Order


class DecimalInput(forms.TextInput):
    input_type = 'number'
    is_hidden = False


class ProductForm(forms.ModelForm):
    CHOICES = [
        ('Laptops', 'Laptops'),
        ('Headphones', 'Headphones'),
        ('Mouses', 'Mouses'),
        ('Keyboards', 'Keyboards'),
        ('Other', 'Other')
    ]
    category = forms.ChoiceField(choices=CHOICES, initial='Other', label="Category")

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'remain', 'cost']
        labels = {
            'product_name': 'Product',
            'description': 'Description',
            'image': 'Image',
            'remain': 'Remain',
            'cost': 'Cost'
        }
        widgets = {
            'remain': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'cost': DecimalInput(attrs={'class': 'form-control'})
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Find')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'phone', 'address']
        labels = {
            'username': 'Name',
            'phone': 'Phone number',
            'address': 'Address',
        }
