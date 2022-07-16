from django.shortcuts import render
from django.http import HttpResponse

def welcome_blog(request):
    return HttpResponse('<h1>Welcome To My Blog</h1>')
