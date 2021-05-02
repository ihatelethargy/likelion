from django.shortcuts import render, get_object_or_404, redirect
# Blog model 임폴트 과정이 꼭 필요함
from .models import Blog  
# Create your views here.
from django.utils import timezone

def home(request):
    ## models 연결하고 저장
    blogs = Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog,pk=id)
    return render(request, 'detail.html', {'blog':blog})    

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)