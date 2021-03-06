from django.shortcuts import render,get_object_or_404
from .models import Blog                                         #to get blogs data import model 1


def allblogs(request):
    blogs = Blog.objects.all()                                         #to get blog data from the database create object 2
    return render(request, 'blog/allblog.html', {'blogs': blogs})     #create a context here blogs 3


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
