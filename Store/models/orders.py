import datetime
from django.db import models

from .products import Products
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=2000, default='')
    phone = models.CharField(max_length=15, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
         self.save()

    @staticmethod
    def get_orders_by_Customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by("-date")
