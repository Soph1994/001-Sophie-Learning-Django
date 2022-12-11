from django.urls import include, path

from .views import BlogListView, BlogView

urlpatterns = [
    path('', BlogView.as_view(), ),
    path('blogs/', BlogListView.as_view()),
]