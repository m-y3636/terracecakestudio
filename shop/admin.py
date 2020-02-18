from django.contrib import admin
from shop.models import Category, Tag, Post, ContentImage, Photos

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(ContentImage)
admin.site.register(Photos)