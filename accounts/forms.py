from django import forms
from django.db.models import indexes, query
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from .models import Customer, Order, Product

STATUS = (
    ('Pending', 'Pending'),
    ('Out for delivery', 'Out for delivery'),
    ('Delivered', 'Delivered'),
)


class CreateCustomer(ModelForm):
    class Meta:
        model =  Customer
        fields = ['name', 'phone', 'email', 'address']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
        }


class CreateProduct(ModelForm):
    class Meta:
        model =  Product
        fields = ['name', 'price', 'category', 'description', 'tags']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'category': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }


class CreateOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']
        widgets = {
            # ,widget={'class': 'form-control'}
            'customer': forms.Select(choices=Order.objects.all(), attrs={'class': 'form-control'}),
            'product': forms.Select(choices=Product.objects.all() ,attrs={'class': 'form-control'}),
            'status': forms.Select(choices=STATUS, attrs={'class': 'form-control'})
        }
