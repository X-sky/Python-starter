from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path("list/", views.blog_list, name="blog_list"),
    path("new_blog/", views.new_blog, name="new_blog"),
]