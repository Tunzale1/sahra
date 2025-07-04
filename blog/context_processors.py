from .models import Blog

def blogs_processor(request):
    blogs = Blog.objects.all()
    return {'blogs': blogs}
