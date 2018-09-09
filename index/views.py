from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_1_views(request):
    return render(request, 'index_1.html')

def blog_post_views(request):
    return render(request, 'blog-post.html')