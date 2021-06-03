from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from blog.models import Blog

class BlogList(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 2



class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'


class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'text', 'created_date', 'published_date']
    template_name = 'blog/blog_new.html' # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'text', 'published_date']
    template_name = 'blog/blog_update.html'  # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')