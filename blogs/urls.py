from django.urls import include, path

from .views import BlogView

urlpatterns = [
    path('blogs/', BlogView.as_view(), ),
]