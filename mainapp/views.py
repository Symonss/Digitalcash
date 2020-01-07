from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category, Opportunity
from django.http import HttpResponse
from django.views import View


def home(request):
    opps = Opportunity.published.all()
    stories = Post.approved.all()[:6]
    context={
        'opps': opps,
        'stories': stories
    }
    return render(request, 'index.html', context)

def post_detail_view(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    recent = Post.published.all()[:5]
    categories = Category.objects.all()
    context = {
        'post': post,
        'recent': recent,
        'categories': categories,
    }
    return render(request, 'post_detail.html', context)

def opportunity_detail_view(request, opp):
    opportunity = get_object_or_404(Opportunity, slug=opp, status='published')
    recent = Post.published.all()[:5]
    categories = Category.objects.all()
    context = {
        'post': post,
        'recent': recent,
        'categories': categories,
    }
    return render(request, 'opportunity_detail.html', context)



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
    return render(request, 'post_list.html', {'posts': posts})
