from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.userRegister, name='userRegister'),
    path('login/', views.login, name='login'),
]