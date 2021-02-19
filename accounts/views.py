from django.shortcuts import redirect, render
from .models import Customer,Product, Order

# Forms
from .forms import (
    CreateCustomer, 
    CreateOrder, 
    CreateProduct, 
    LoginForm,
    RegisterForm
)

# Create your views here.

# ------------------------ READ ------------------------
def home_view(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    order_count = Order.objects.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'order_count': order_count,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)

def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'accounts/products.html', context)

def customers_view(request):
    customers = Customer.objects.all()

    context = {
        'customers': customers
    }
    return render(request, 'accounts/customers.html', context)

def customer_view(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count
    }
    return render(request, 'accounts/customer.html', context)


# ------------------------ CREATE ------------------------
def create_customer(request):
    form = CreateCustomer()

    if request.method == 'POST':
        form = CreateCustomer(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')

    context = {
        'form': form 
    }

    return render(request, 'accounts/create.html', context)

def create_order(request):
    form = CreateOrder()

    if request.method == 'POST':
        form = CreateOrder(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'accounts/create.html', context)

def create_product(request):
    form = CreateProduct()
    if request.method == 'POST':
        form = CreateProduct(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/products/')
            
    context = {
        'form': form
    }
    return render(request, 'accounts/create.html', context)

def customer_create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CreateOrder(initial={'customer': customer})
    if request.method == 'POST':
        form = CreateOrder(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(f'/customers/{customer.id}')
    
    context = {
        'form': form
    }
    return render(request, 'accounts/create.html', context)

# ------------------------ DELETE ------------------------
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('/')

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('/')

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/products/')


# ------------------------ UPDATE ------------------------
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = CreateProduct(instance=product)

    if request.method == 'POST':
        form = CreateProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    context = {
        'form': form
    }
    return render(request, 'accounts/create.html', context)

def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = CreateOrder(instance=order)

    if request.method == 'POST':
        form = CreateOrder(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'accounts/create.html', context)

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CreateCustomer(instance=customer)

    if request.method == 'POST':
        form = CreateCustomer(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'accounts/create.html', context)


# ------------------------ AUTH ------------------------
def login_view(request):
    form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
            
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)