from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category, Opportunity, User
from django.http import HttpResponse
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib import messages
from .forms import OppUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def home(request):
    opps = Opportunity.approved.all()
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
    opportunity = get_object_or_404(Opportunity, slug=opp, status='approved')
    recent = Opportunity.approved.all()[:5]
    categories = Category.objects.all()
    context = {
        'opportunity': opportunity,
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

@login_required
def administration(request):
    opps = Opportunity.objects.all().filter(status = 'inreview')
    stories = Post.objects.all().filter(status = 'inreview')
    context={
        'opps': opps,
        'stories': stories
    }
    return render(request, 'administration/dashboard.html', context)

def ff(request):
    return render(request, 'administration/formss.html',{})

class OppCreatView(CreateView):
    model = Opportunity
    fields = ('title','direct_link','category','types','description','img')
    template_name = 'administration/opp_add_form.html'

    def form_valid(self, form):
        opp = form.save(commit=False)
        opp.author = self.request.user
        opp.least_amount = '00'
        opp.save()
        messages.success(self.request, 'Opportunity Succesfully Created Finish up!')

        return redirect('opp_update',pk=opp.pk)

class OppUpdate(UpdateView):
    model = Opportunity
    form_class = OppUpdateForm
    template_name = 'administration/update_form.html'

class CatCreatView(CreateView):
    model = Category
    fields = ('title','description')
    template_name = 'administration/cat_add_form.html'

    def form_valid(self, form):
        cat = form.save(commit=False)
        cat.save()
        messages.success(self.request, 'Category Succesfully Created!')

        return redirect('admins')