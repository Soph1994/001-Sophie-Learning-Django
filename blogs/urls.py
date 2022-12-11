from django.urls import include, path

from .views import BlogeCreateView, BlogListView, BlogView

urlpatterns = [
    path('', BlogView.as_view(), ),
    path('blogs/', BlogListView.as_view(),name='blog_list'),
    path('blogs/create/', BlogeCreateView.as_view(),name='blog_create'),
]