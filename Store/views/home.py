from django.http import HttpResponse
from django.shortcuts import render, redirect
from Store.models.products import Products
from Store.models.Category import Category
from django.views import View


class Index(View):

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        category = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Products.get_all_products_by_id(categoryID)
        else:
            products = Products.get_all_products()
        data = {'products': products, 'categories': category}
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect('homepage')
