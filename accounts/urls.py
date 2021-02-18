from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name="dashboard"),
    path('products/',views.products_view, name="products"),
    path('customers',views.customers_view, name="customers"),
    path('customers/<str:pk>',views.customer_view, name="customer"),

    path('create_customer/', views.create_customer, name="create_customer"),
    path('create_order/', views.create_order, name="create_order"),
    path('create_product/', views.create_product, name="create_product"),

    path('delete_order/<str:pk>', views.delete_order, name="delete_order"),
    path('delete_customer/<str:pk>', views.delete_customer, name="delete_customer"),
    path('delete_product/<str:pk>', views.delete_product, name="delete_product"),

    path('update_order/<str:pk>', views.update_order, name="update_order"),
    path('update_customer/<str:pk>', views.update_customer, name="update_customer"),
    path('update_product/<str:pk>', views.update_product, name="update_product"),
]