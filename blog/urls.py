from django.conf.urls import patterns, include, url
urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'toy_blog.views.home', name='home'),
    # url(r'^toy_blog/', include('toy_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'index'),
    url(r'^cms/$', 'cms'),
    url(r'^cms/new/$', 'new_post'),
    url(r'^(?P<slug>[-\w]+)/$', 'detail'),
    # Uncomment the next line to enable the admin:
)
