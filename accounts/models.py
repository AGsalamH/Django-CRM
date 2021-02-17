from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(null= True, max_length=50)
    email = models.CharField(null= True, max_length=150)
    address = models.CharField(null= True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=False, null=True, default=timezone.now)

    def __str__(self):
        return self.name



class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    
    name = models.CharField(max_length = 200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    date_created = models.DateTimeField(auto_now_add=False, null=True, default=timezone.now)
    description = models.CharField(max_length=300, null=True)
    tags = ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, default='Pending')
    date_created = models.DateTimeField(auto_now_add=False, null=True, default=timezone.now)

    def __str__(self):
        return f'{self.customer}\'s Order'
    

