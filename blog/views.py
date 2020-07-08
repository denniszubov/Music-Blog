from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import BlogPost


# Create your views here.
def blog(request):
    return HttpResponse("<h1>Blog Home</h1>")


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blog_posts.html"
    context_object_name = "blog_posts"
