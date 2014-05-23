from django.conf.urls import patterns, url
from views import PostListing


urlpatterns = patterns('post.urls',
    url(r'^$', PostListing.as_view(), name='listing'),
)