from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def index(request):
    return HttpResponse("Hello, world. Welcome to Kyntra.")

def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html', {'name':'admin_dashboard'})

def admin_buyers(request):
    return render(request,'admin/admin_buyers.html', {'name':'admin_buyers'})

def admin_sellers(request):
    return render(request,'admin/admin_sellers.html', {'name':'admin_sellers'})

def admin_products(request):
    return render(request,'admin/admin_products.html', {'name':'admin_products'})