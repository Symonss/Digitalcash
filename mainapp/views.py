from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
from django.http import HttpResponse
from django.views import View

 
def home(request):
    posts = Post.published.all()[:15]
    return render(request, 'home.html', {'posts':posts})

def index(request):
    posts = Post.published.all()[:15]
    return render(request, 'index.html', {'posts':posts})

def post_detail_view(request,post):
    post = get_object_or_404(Post, slug=post, status='published')
    print(post)
    recent = Post.published.all()[:5]
    categories = Category.objects.all()
    context = {
        'post':post,
        'recent':recent,
        'categories': categories,
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'posts':posts})
