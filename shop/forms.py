from django.forms import ModelForm
from shop.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields='__all__'

class PostSearchForm():
    class Meta:
        model = Post
        fields='__all__'
