from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.index,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logoutuser',views.logoutuser,name='logoutuser'),
    path('rooms',views.rooms,name='rooms'),
    path('mybookings',views.mybookings,name='mybookings'),

]