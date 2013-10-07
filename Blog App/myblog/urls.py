from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post, Author
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(
                           queryset=Post.objects.all().order_by("-date")[:2],
                           template_name="index.html")),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(
                           model=Post,
                           template_name="post.html")),
	url(r'^archives/$', ListView.as_view(
                           queryset=Post.objects.all().order_by("-date"),
                           template_name="archives.html")),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
