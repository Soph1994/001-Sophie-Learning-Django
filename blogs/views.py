from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from .models import Post

# Create your views here.


class BlogView(TemplateView):
    template_name = 'blogs/blog.html'


class BlogListView(ListView):
    model           = Post
    template_name   = 'blogs/blog_list.html'


class BlogeCreateView(CreateView):
    model           = Post
    template_name   = 'blogs/blog_create.html'
    fields          = [
        'title',
        'category',
        'content',
    ]
    success_url     = reverse_lazy('blog_list')