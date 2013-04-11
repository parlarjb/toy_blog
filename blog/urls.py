from django.conf.urls import patterns, include, url
from blog.models import Post
from django.views.generic import TemplateView, ListView

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(model=Post,
                                context_object_name="post_list",
                                paginate_by=5)),
    url(r'^cms/$', 'cms'),
    url(r'^cms/new/$', 'new_post'),
    url(r'^cms/edit/(?P<slug>[-\w]+)/$', 'edit_post'),
    url(r'^cms/delete/(?P<slug>[-\w]+)/$', 'delete_post'),
    url(r'^cms/canceled/$', TemplateView.as_view(template_name='blog/canceled.html')),
    url(r'^cms/deleted/$', TemplateView.as_view(template_name='blog/deleted.html')),
    url(r'^(?P<slug>[-\w]+)/$', 'detail'),
    # Uncomment the next line to enable the admin:
)
