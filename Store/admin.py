from django.contrib import admin
from .models.products import Products
from .models.Category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminOrders(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity', 'date']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'phone', 'email']


admin.site.register(Products, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrders)
