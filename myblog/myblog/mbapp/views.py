from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

# Create your views here.

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'index.html')

def new(request):
    form = BlogForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('/blog/'+str(new_blog.id))
    return redirect('/home/')
    
    # new_blog = Blog()
    # new_blog.title = request.POST['title']
    # new_blog.writer = request.POST['writer']
    # new_blog.body = request.POST['body']
    # new_blog.pub_date = timezone.now()
    # new_blog.image = request.FILES['image']
    # new_blog.save()
    # return redirect('/blog/'+str(new_blog.id))

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('/blog/' +str(update_blog.id))    

def detail(request, id):
    blog = get_object_or_404(Blog,pk=id)
    return render(request, 'detail.html', {'blog':blog})

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')  