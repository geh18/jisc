from django.contrib import admin

from django.contrib import admin
from .models import Post, Tags


class PostsAdmin(admin.ModelAdmin):
    pass


class TagsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostsAdmin)
admin.site.register(Tags, TagsAdmin)
