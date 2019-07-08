# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .business import *
from .models import StudentInfo
# Create your views here
from django.contrib.auth.decorators import login_required


def registered_data(request):
    print("Registered")
    datastore(request)
    return render(request, 'submit.html')

def login_user(request):


    if request.method == "POST":
        # get username from request
        username = request.POST['username']
        # get password from request
        password = request.POST['password']
        # check if username is present in database
        if StudentInfo.objects.filter(username=username).exists():
            # check if password from request is same as password in database
            if StudentInfo.objects.filter(password=password).exists():
                print("User verified")
                request.session['username'] = username
                return HttpResponseRedirect(reverse('Home Page'))
            # else prompt message to user that invalid password
            else:
                return HttpResponse("Wrong password!!")
        else:
            # else prompt message to user that invalid username
            return HttpResponse("Wrong username!!")

    else:
        print("Error")
        return render(request, 'submit.html')

def login_success(request):
    print("Login successful")

    if request.session.has_key('username'):
        print("session key is verified")
        username = request.session['username']
        return render(request, 'home.html', {"username": username})

    return HttpResponseRedirect(reverse('Login Page'))

def logout_user(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('Login Page'))





