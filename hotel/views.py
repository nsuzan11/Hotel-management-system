from re import template
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    return render(request,'index.html')
    # template = loader.get_template('myfirst.html')
    # return HttpResponse("Hello world!!")
    #return HttpResponse(template.render())