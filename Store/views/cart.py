from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password
from Store.models.customer import Customer
from Store.models.products import Products


class Cart(View):

    def get(self, request):
        if request.session.get('cart') is None:
            request.session.cart = {}
            return render(request, 'cart.html')

        else:
            ids = list(request.session.get('cart').keys())
            products = Products.get_all_products_id(ids)
            return render(request, 'cart.html', {'products': products})
