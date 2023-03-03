from django.contrib import admin
from django.shortcuts import render
from casinoproject1 import views


def index(request):
    return render(request, 'index.html')