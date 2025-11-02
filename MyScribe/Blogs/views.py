from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def landing_page(request):
    return render (request, "Blogs/landing.html")

@login_required
def home_page(request):
    context = {'blogs' : Blog.objects.all()}
    return render (request, "Blogs/home.html",context)

def details_page(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, 'Blogs/details.html', context)

@login_required
def create_blog(request):
    form = BlogForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect ("Blogs:home")
    context = {'form':form}
    return render (request, 'Blogs/create.html',context)

@login_required
def update_page(request):
    context = {'blogs' : Blog.objects.all()}
    return render (request, 'Blogs/update.html',context)

@login_required
def edit_blog(request,id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect ("Blogs:home")
    context = {'form':form}
    return render(request, 'Blogs/edit.html', context)

@login_required
def delete_blog(request):
    blogs = Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render (request, "Blogs/delete.html", context)

@login_required
def trash_blog(request,id):
    blog = Blog.objects.get(id=id)
    if request.method=="POST":
        blog.delete()
        return redirect ("Blogs:home")
    context = {'blog':blog}
    return render (request, 'Blogs/trash.html', context)