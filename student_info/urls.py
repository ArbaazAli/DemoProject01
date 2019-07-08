from django.urls import path
from .import views

urlpatterns = [

    path('submit/', views.registered_data, name ='Submit Page'),
    path('login/', views.login_user, name='Login Page'),
    path('logout/', views.logout_user, name='Logout Page'),
    path('success/', views.login_success, name='Home Page')


]



