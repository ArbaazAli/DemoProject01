# I have created this fie
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')

def end(request):
    return render(request, 'end.html')

def login(request):
    return render(request, 'login.html')

