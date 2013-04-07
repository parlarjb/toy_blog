from django.db import models
from django.conf import settings
from blog.models import Post

MAX_LENGTH = getattr(settings, "MAX_COMMENT_NAME_LENGTH", 128)
# Create your models here.

class Comment(models.Model):
    post= models.ForeignKey(Post)
    parent_comment = models.ForeignKey('self', null=True, blank=True, default=None)
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=MAX_LENGTH)
    body = models.TextField()
