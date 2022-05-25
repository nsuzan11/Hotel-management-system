from re import template
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.

# def index(request):
#     print("hello")
#     return render(request, 'index.html')

# class index(TemplateView):
#     template_name = " "

def index(request):
    print("aboutus")
    return render(request, 'index.html')
    
def aboutus(request):
    print("aboutus")
    return render(request, 'aboutus.html')

def rooms(request):
    return render(request, 'rooms.html')

def book(request):
    return render(request, 'book.html')

def contactus(request):
    return render(request, 'contactus.html')
    
def login(request):
    return render(request, 'login.html')
    # template = loader.get_template('myfirst.html')
    # return HttpResponse("Hello world!!")
    #return HttpResponse(template.render())