# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, RequestContext
from blog.models import Post

from django.http import HttpResponse

def index(request):
    latest_blog_list = Post.objects.all().order_by('-date')[:5]
    return render_to_response('blog/index.html', {'latest_blog_list':latest_blog_list})

def cms(request):
    return HttpResponse("Manage")

def new_post(request):
    if request.POST:
        print "HAVE POST", request.POST
    return render_to_response('blog/new_post.html', {}, context_instance = RequestContext(request))


def detail(request, slug):
    p = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/detail.html', {'post':p})
