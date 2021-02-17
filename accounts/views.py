from django.shortcuts import redirect, render
from .models import Customer,Product, Order

# Forms
from .forms import CreateCustomer, CreateOrder

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
    
def customer_view(request, pk):
    order_count = Order.objects.count()
    customer = Customer.objects.get(id=pk)
    customer_orders = customer.order_set.all()
    print(customer_orders)
    context = {
        'customer': customer,
        'order_count': order_count,
        'customer_orders': customer_orders
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

    return render(request, 'accounts/create_customer.html', context)


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
    return render(request, 'accounts/create_order.html', context)


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

