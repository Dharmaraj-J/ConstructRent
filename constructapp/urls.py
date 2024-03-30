from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.indexpage,name='indexpage'),

    path('loginpage/',views.loginpage,name='loginpage'),
    path('handellogin',views.handellogin, name='handellogin'),

    path('registerpage/',views.registerpage,name='registerpage'),
    path('handleregister',views.handleregister, name='handleregister'),


    path('handlelogout/',views.handlelogout, name='handlelogout'), 


    path('addequipment',views.addequipment, name='addequipment'),
    path('add',views.add, name='add'),

    path('deleteequipment',views.deleteequipment, name='deleteequipment') ,
    path('delete/<str:slug>',views.delete, name='delete'),

    path('edit/<str:slug>',views.edit, name='edit'),


    path('customerpage/',views.customerpage,name='customerpage'),
    path('rentalmanagerpage/',views.rentalmanagerpage,name='rentalmanagerpage'),

    path('requests',views.requests, name='requests'),
    path('apply/<str:slug>',views.apply, name='apply'),
    path('denied_request/<str:slug>',views.denied_request, name='denied_request'),
    path('accept_request/<str:slug>',views.accept_request,name='accept_request'),

    path('searchpage',views.searchpage,name="searchpage"),

    # path('otp_view',views.otp_view,name= 'otp_view' ),


]
