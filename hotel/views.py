import email
from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from idna import check_initial_combiner
from requests import request
from .models import Booking,Room
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# login_required(login_url ='login')
def index(request):
    print("hello")
    return render(request, 'index.html')

@login_required(login_url='/login/')
def rooms(request):
    return render(request, 'rooms.html')

@login_required(login_url='/login/')
def book(request):
    if(request.method == "POST"):
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        room_type = request.POST.get('roomtype')
        no_people = request.POST.get('nopeople')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        room_type_model = Room.objects.filter(room_type = room_type)[0]
        instance = Booking(
            room_type = room_type_model,
            user_info = request.user,
            start_day = check_in,
            end_day = check_out,
            phone_number = phone_number,
            email = email,
            no_people = no_people
            )
        instance.save()

    return render(request, 'book.html')

def contactus(request):
    return render(request, 'contactus.html')
    
def loginP(request):
    return render(request, 'login.html')

# def booknow(request):
#     if(request.method == "POST"):
#         form = BookForm(request.POST)
#         if(form.is_valid()):
#             fullname = form.cleaned_data['fullname']
#             checkin = form.cleaned_data['checkin']
#             checkout = form.cleaned_data['checkout']
#             roomtype = form.cleaned_data['roomtype']
#             nopeople = form.cleaned_data['nopeople']
#             email = form.cleaned_data['email']
#             phone_number = form.cleaned_data['phone_number']
#             instance = Booking(
#                 room_type=roomtype,
#                 user_info = fullname,
                
#             )

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created for '+ user)

            return redirect('/login')

    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
        
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')