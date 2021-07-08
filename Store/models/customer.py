from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def emailExist(self):
        return Customer.objects.filter(email=self.email)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def __str__(self):
        return self.firstname
