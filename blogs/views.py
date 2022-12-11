from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView

from .models import Post

class BlogView(TemplateView):
    template_name = 'blogs/blog.html'


class BlogListView(ListView):
    model           = Post
    template_name   = 'blogs/blog_list.html'

