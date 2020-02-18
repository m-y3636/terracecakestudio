from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from shop.models import Post, Category, Tag, ContentImage, Photos
from pure_pagination.mixins import PaginationMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils import timezone

from shop.forms import PostForm, PostSearchForm

# Create your views here.
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj

class IndexView(TemplateView):
    model = Post
    template_name = 'shop/top.html'
    context_object_name='post'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(category__name__icontains=query)|
            Q(tags__name__icontains=query)
        )
        if query is not None:
            qs=super().get_queryset().filter(lookups).distinct()
            return qs
        
        else:
            qs=super().get_queryset().filter().distinct()
            return qs
        

class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True))
    )
    template_name='shop/category.html'

class TagListView(ListView):
    queryset = Tag.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)
    ))
    template_name="shop/tag.thml"

class PhotoView(ListView):
    model = Photos
    template_name="photo/photo_list.html"

class PhotoDetailView(DetailView):
    model = Photos

class PostForm(CreateView):
    template_name = "blog/post_input.html"
    form_class = PostForm
    success_url = '../blog'

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        return super().form_valid(form)
 
    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        return super().form_invalid(form)

class SearchPostForm(ListView):
    template_name= PostListView
    model = Post
    form =  PostSearchForm

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(category__name__icontains=query)|
            Q(tags__name__icontains=query)
        )
        if query is not None:
            qs=super().get_queryset().filter(lookups).distinct()
            return qs