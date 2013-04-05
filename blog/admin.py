from blog.models import Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'date', 'body']
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
