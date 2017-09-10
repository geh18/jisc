from django.contrib import admin

from django.contrib import admin
from .models import Post, Tags


class PostsAdmin(admin.ModelAdmin):
    readonly_fields = ['viewed']
    list_display = ('title', 'publish', )
    list_filter = ('author', )

class TagsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostsAdmin)
admin.site.register(Tags, TagsAdmin)
