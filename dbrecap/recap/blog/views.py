from django.shortcuts import render, get_object_or_404
# Blog model 임폴트 과정이 꼭 필요함
from .models import Blog  
# Create your views here.

def home(request):
    ## models 연결하고 저장
    blogs = Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog,pk=id)
    return render(request, 'detail.html', {'blog':blog})    
