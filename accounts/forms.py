from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea
from .models import Customer, Order, Product

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  get_user_model

UserModel = get_user_model()

STATUS = (
    ('Pending', 'Pending'),
    ('Out for delivery', 'Out for delivery'),
    ('Delivered', 'Delivered'),
)

CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Out Door', 'Out Door')
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
        fields = ['name', 'price', 'category', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORY, attrs={'class': 'form-control'}),
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

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.widgets.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'firstname'
            }),
            'last_name': forms.widgets.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'lastname'
            }),
            'username': forms.widgets.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email here ...'
            })    
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.widgets.Input(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget = forms.widgets.Input(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Confirm password'
        })


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control'
        }) 
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
            'class': 'form-control'
        })
