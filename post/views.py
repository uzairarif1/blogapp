from django.shortcuts import render
# from django.contrib import 
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()
    return render(request, 'index.html',{'post':post})

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html',{'y':post})