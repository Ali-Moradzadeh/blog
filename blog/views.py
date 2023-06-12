from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.published.all()
    
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page", 1)
    try:
        page_number = min(int(page_number), paginator.num_pages)
    except ValueError:
        page_number = 1
    posts = paginator.page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})