from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs_list = Blog.objects.all().order_by('-created_at')  # optional ordering

    paginator = Paginator(blogs_list, 3)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    other_blogs = Blog.objects.exclude(slug=slug)[:6]
    return render(request, 'blog-details.html', {'blog': blog, 'other_blogs': other_blogs})

