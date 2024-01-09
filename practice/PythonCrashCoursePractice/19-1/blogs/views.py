from django.shortcuts import render

from .models import BlogPost


# Create your views here.
def blog_list(request):
    context = {"blogs": BlogPost.objects.order_by("date_added"), "title": "Blog List"}
    return render(request, "blogs/blog_list.html", context)
