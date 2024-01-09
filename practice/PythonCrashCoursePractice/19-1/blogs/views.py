from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm


# Create your views here.
def blog_list(request):
    """展示博客列表"""
    context = {"blogs": BlogPost.objects.order_by("date_added"), "title": "Blog List"}
    return render(request, "blogs/blog_list.html", context)


def new_blog(request):
    """创建新博客"""
    if request.method != "POST":
        # 未提交数据：创建一个新表单
        form = BlogForm()
    else:
        # POST提交的数据，对数据进行处理
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog_list")

    context = {"form": form, "title": "Create Blog"}
    return render(request, "blogs/create_blog.html", context)
