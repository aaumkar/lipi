from django.http import request
from django.shortcuts import render

# Create your views here.


def show(request):
    return render(request, 'main/index.html', {})


def teental(request):
    return render(request, 'main/teental.html', {})
