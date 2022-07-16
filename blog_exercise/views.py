from django.shortcuts import render
from django.http import HttpResponse

def welcome_blog(request):
    return render(request, 'blog_home.html')
