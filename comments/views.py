# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

from blog.models import Post
from comments.forms import CommentForm
from comments.models import Comment

def create_comment(request, slug):
    print "SLUG IS", slug
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            parent_comment = form.cleaned_data['parent']
            if not parent_comment:
                parent_comment = None
            comment = Comment.objects.create(author=author, body=body, post=post, parent_comment=parent_comment)
            return HttpResponseRedirect('/%s/' % slug)
        else:
            print "Bad comment data"
    comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'post':post, 'comment_form':comment_form, 'slug':slug})


