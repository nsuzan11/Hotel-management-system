from django.contrib import admin
from django.urls import path
from hotel.views import index
from django.urls import include, re_path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

app_name = 'hotel'
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    # re_path(r'^/login/' , login.views.login_view),
    path('login/',views.loginPage, name="login"),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout/', views.logoutUser, name="logout"), 
    path('', index),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('rooms/', rooms),
    path('book/', book),
    path('contactus/', contactus),
    # path('book-now',booknow ),

]
