from django.urls import path

from shop.views import IndexView, PostDetailView, CategoryListView, TagListView, PostListView, PhotoView, PostForm

app_name = 'shop'
urlpatterns = [
    path('', IndexView.as_view(), name = 'top'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('blog/', PostListView.as_view(), name = 'blog'),
    path('categories/', CategoryListView.as_view(), name = 'category_list'),
    path('tags/', TagListView.as_view(), name = 'tag_list'),
    path('photo/', PhotoView.as_view(), name='photo'),
    path('input/', PostForm.as_view(), name='input'),
]