from django.shortcuts import render
from django.views import View
from Store.models.orders import Order


class Orders(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_Customer(customer)
        return render(request, "order.html", {'orders': orders})
