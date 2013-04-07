from django.conf.urls import patterns, include, url


urlpatterns = patterns('comments.views',
    url(r'^post/(?P<slug>[-\w]+)/$', 'create_comment', ),
)
