# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.views.decorators.cache.cache_page
from blog.models import Post
from blog.forms import PostForm
from comments.forms import CommentForm

from django.http import HttpResponse, HttpResponseRedirect

def is_staff(function):
    def new_func(request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponse("Not a staff member!")
        return function(request, *args, **kwargs)
    return new_func

@cache_page(10)
def index(request):
    latest_blog_list = Post.objects.all().order_by('-date')[:5]
    return render_to_response('blog/index.html', {'latest_blog_list':latest_blog_list})

def cms(request):
    return HttpResponse("Manage")



@login_required
@is_staff
def new_post(request):
    if request.method == 'POST':
        if '_cancel' in request.POST:
            return HttpResponseRedirect('/')
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            slug = form.cleaned_data['slug']
            date = form.cleaned_data['date']
            post = Post.objects.create(title=title, body=body, slug=slug, date=date)
            return HttpResponseRedirect('/%s/' % slug)
        else:
            print "Bad form data"
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form':form, 'action':'/cms/new/'})

@cache_page(10)
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.slug = form.cleaned_data['slug']
            post.date = form.cleaned_data['date']
            post.save()
            return HttpResponseRedirect('/%s/' % slug)
    else:
        post_data = {'title': post.title,
                     'body': post.body,
                     'slug': post.slug,
                     'date': post.date
                     }
        form = PostForm(initial = post_data)
    return render(request, 'blog/new_post.html', {'form':form, 'title':'Edit Post', 'action':'/cms/edit/%s/'%slug})

@login_required
@is_staff
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        print request.POST
        if '_cancel' in request.POST:
            print "Cancelled"
            return HttpResponseRedirect('/cms/canceled')
        elif '_delete' in request.POST:
            print "Deleted"
            post.delete()
            return HttpResponseRedirect('/cms/deleted')
    return render(request, 'blog/delete_post.html', {'post':post, 'path':request.get_full_path})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    comments = post.comment_set.all().order_by('date_time')
    context = {'post':post, 'comment_form':comment_form, 'slug':slug, 'comments':comments}
    return render(request, 'blog/detail.html', context)
