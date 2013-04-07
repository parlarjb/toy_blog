from comments.models import Comment
from django.contrib import admin

class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'body']
    list_display = ('author', 'date_time')
    readonly_fields = ("date_time",)

admin.site.register(Comment, CommentAdmin)
