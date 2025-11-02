from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from Blogs.models import Blog
# Create your views here.

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data.get("username")
            messages.success(request,f"Welcome {userName}, Your account has been created!")
            return redirect ("Auth:login")
    form = RegisterForm()
    context = {
        'form':form
    }
    return render (request, "Auth/register.html",context)

@login_required
def logout_view(request):
    logout(request)
    return render (request,'Auth/logout.html')

def auth_view(request):
    if not request.user.is_autheticated:
        return redirect ('Blogs:landing')
    return render("Blogs:home")

@login_required
def profile_view(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog
    }
    return render (request, "Auth/profile.html", context)