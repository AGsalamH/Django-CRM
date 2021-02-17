from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name="home"),
    path('products/',views.products_view, name="products"),
    path('customer/<str:pk>',views.customer_view, name="customer"),
    path('create_customer/', views.create_customer, name="create_customer"),
    path('create_order/', views.create_order, name="create_order"),

    path('delete_order/<str:pk>', views.delete_order, name="delete_order"),
    path('delete_customer/<str:pk>', views.delete_customer, name="delete_customer"),
    path('delete_product/<str:pk>', views.delete_product, name="delete_product"),
]