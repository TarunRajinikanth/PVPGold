from django.shortcuts import redirect
from django.views import View
from Store.models.customer import Customer
from Store.models.products import Products
from Store.models.orders import Order


class Checkout(View):

    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Products.get_all_products_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)) )
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('orders')
