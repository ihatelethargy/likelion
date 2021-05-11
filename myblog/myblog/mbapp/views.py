from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})