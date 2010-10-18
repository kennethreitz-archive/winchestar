from django.conf.urls.defaults import *
from ripper.views import LatestArticlesFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wincstar/', include('wincstar.foo.urls')),
#	(r'^wincstar/', include('wincstar.ripper.urls')),
	(r'^secret/', 'ripper.views.index'),
	(r'^article/(?P<article_slug>[a-zA-Z0-9_\-]+)/$', 'ripper.views.detail'),
	(r'^rss/$', LatestArticlesFeed()),
#	r'^latest/feed/$', LatestEntriesFeed()),
#	(r'^polls/$', 'polls.views.index'),
#    (r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	# (r'^', 'ripper.views.index'),
)
