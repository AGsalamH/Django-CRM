from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Customer,Product, Order
from django.contrib import messages
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
@login_required(login_url='login')
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'accounts/delete.html',  context)

@login_required
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {
        'item': customer
    }
    return render(request, 'accounts/delete.html',  context)

@login_required
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {
        'item': product
    }
    return render(request, 'accounts/delete.html',  context)


# ------------------------ UPDATE ------------------------
@login_required
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

@login_required
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

@login_required
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

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['isAuth'] = True
            nxt = request.GET.get('next')
            if nxt:
                return redirect(nxt)
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/login/')
            
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login/')