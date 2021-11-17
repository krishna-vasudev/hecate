from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("login/<str:usertype>", views.loginUser, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("signup/<str:usertype>", views.signupuser, name='signup'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
