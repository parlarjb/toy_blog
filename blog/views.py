# Create your views here.
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import loader, RequestContext
from blog.models import Post
from blog.forms import PostForm

from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    latest_blog_list = Post.objects.all().order_by('-date')[:5]
    return render_to_response('blog/index.html', {'latest_blog_list':latest_blog_list})

def cms(request):
    return HttpResponse("Manage")

def new_post(request):
    if request.method == 'POST':
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

def make_post_data(post):
    return post_data

def edit_post(request, slug):
    print request.user
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
    p = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/detail.html', {'post':p})
