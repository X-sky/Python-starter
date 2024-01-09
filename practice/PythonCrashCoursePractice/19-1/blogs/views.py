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


def edit_blog(request, blog_id):
    """编辑既有博客"""
    blog = BlogPost.objects.get(id=blog_id)

    if request.method != "POST":
        # 初次请求，使用当前条目填充表单
        form = BlogForm(instance=blog)
    else:
        # POST提交的数据，对数据进行处理
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:blog_list")

    context = {"blog": blog, "form": form, "title": f"Edit Blog {blog.title}"}
    return render(request, "blogs/edit_blog.html", context)
