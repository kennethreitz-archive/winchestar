# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.syndication.views import Feed

try:
	from collections import OrderedDict
except ImportError:
	from ordereddict import OrderedDict

from ripper.models import Article


class LatestArticlesFeed(Feed):
	title = "Winchester Star Articles"
	link = "http://www.winchesterstar.com/"
	description = "Winchester Star Article aggregation. Do not use if you are not a paid subscriber."
	feed_url="http://74.207.237.53/rss/"

	def items(self):
		return Article.objects.order_by('-published')[:25]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		_content = item.content
		_content += '<hr />'
		_content += '&copy; 2010 The Wincheser Star. Only for use by paid subscribers.'
		return _content

	def item_link(self, item):
		return item.ourl

	def item_pubdate(self, item):
		return item.published
	
def index(request):
	
	articles = OrderedDict()
	
	for article in Article.objects.all().order_by('-published'):
		if not article.published in articles:
			articles[article.published] = []
		articles[article.published].append(article)
#
#	print
#	print
#	print [(k, 0) for k in articles]
#	print
#	print
	# print articles
	
	return render_to_response('index.html', {'articles': articles})


def detail(request, article_slug):

	art = get_object_or_404(Article, pk=article_slug)	
	return render_to_response('detail.html', {'article': art})