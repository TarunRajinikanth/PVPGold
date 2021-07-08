from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from Store.models.customer import Customer
import re


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        return self.registerUser(request)

    def registerUser(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')

        value = {
            'fname': first_name,
            'lname': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(firstname=first_name,
                            lastname=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = None
        error_message = self.CustomerValidation(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            return render(request, 'signup.html', {'error': error_message, 'values': value})

    def CustomerValidation(self, customer):
        error_message = None
        string_check = re.compile('[@_!#$%^&*()<>?/|}{~:0-9]')
        phone_check = re.compile('[+0-9 ]{12}')
        email_check = re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}')
        password_check = re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}')
        if not customer.firstname:
            error_message = "Please enter firstname."
        elif len(customer.firstname) < 4:
            error_message = "Please enter a valid firstname"
        elif string_check.search(customer.firstname) is not None:
            error_message = "Firstname should not contain any special characters."
        elif not customer.lastname:
            error_message = "Please enter lastname."
        elif len(customer.lastname) < 4:
            error_message = "Please enter a valid lastname"
        elif string_check.search(customer.lastname) is not None:
            error_message = "Lastname should not contain any special characters."
        elif not phone_check.findall(customer.phone):
            error_message = "Invalid Phone Number please enter a valid phone number."
        elif not email_check.findall(customer.email):
            error_message = "Invalid Email please enter a valid Email."
        elif not password_check.findall(customer.password):
            error_message = "Please enter password as per the policy."
        elif customer.emailExist():
            error_message = "Email is already registered please try to login..."
        return error_message
