from ast import keyword
from turtle import title
from django.shortcuts import render
from .models import PostModel

# Create your views here.
def blog(request): 
    keyword = request.GET.get("keywordinput") 
    
    if keyword:
        posts= PostModel.objects.filter(title__contains= keyword).values().order_by("-created_at")
    else:
        posts = PostModel.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
        "keywordinput": keyword if keyword else""
    }
    return render(request, 'blog/blog.html', context)

def post(request, id):
    # post = PostModel.objects.filter(id=id).values()[0]
    # post = get_object_or_404(PostModel, pk=id)
    post = PostModel.objects.get(id=id)
    context = {
        "post": post
    }
    
    return render(request, 'blog/post.html', context)
