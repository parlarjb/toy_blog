from django.conf.urls import patterns, url


urlpatterns = patterns('django.contrib.auth.views',
        url(r'^login/$', 'login', {'template_name':'accounts/login.html'}, name='login'),
    url(r'^password_change/$', 'password_change', {'template_name':'accounts/password_change.html'}, name='password_change'),
    url(r'^password_change/done/$', 'password_change_done', {'template_name':'accounts/password_change_done.html'}, name='password_change_done'),
    url(r'^logout/$', 'logout', {"template_name": "accounts/logout.html"}, name='logout'),

)

