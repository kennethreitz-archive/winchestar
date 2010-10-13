#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
import cookielib

from BeautifulSoup import BeautifulSoup
from dateutil.parser import parse as dtime

from django.core.management import setup_environ
from wincstar import settings

os.environ['DJANGO_SETTINGS_MODULE'] ='wincstar.settings'
setup_environ(settings)

from wincstar.ripper.models import Article as DjangoArticle



class Article(object):
	"""An article."""

	def __init__(self):
		self.title = None
		self.subtitle = None
		self.published = None
		self.author = None
		self.content = None

	def to_django(self):



		art = DjangoArticle()
		art.title = self.title
		art.subtitle = self.subtitle
		art.published = dtime(self.published)
		art.author = self.author
		art.content = self.content

		
		if len(self.content) > 300:
			art.save()
		else:
			print('%s had no usable content.' % (self.title if self.title else ''))




def get_article(url):
	"""Fetches article."""

	return urllib2.urlopen(url).read()


def get_articles():
	opener = urllib2.build_opener(
			urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
	opener.addheaders.append(
			('Content-Type', 'application/x-www-form-urlencoded'))
	login_data = r'_method=POST&data%5BMember%5D%5Bemail%5D=thepythonist%40gmail.com&data%5BMember%5D%5Bpassword%5D=UXe1b&data%5BMember%5D%5Bremember%5D=0'
	opener.open('http://www.winchesterstar.com/members/login',
				login_data).read()
	content = opener.open('http://www.winchesterstar.com/members/login',
						  login_data).read()
	soup = BeautifulSoup(content)
	links = []
	for link in [str(l['href']) for l in soup.findAll('a') if
				 'homepage_links' in l['href']]:
		c = opener.open('http://www.winchesterstar.com/%s' % link)
		links.append(c.geturl())

	return links


def parse_article(content):
	"""Returns article object from given article content."""

	article = Article()

	art = max(BeautifulSoup(content).findAll('td'), key=len)

	article.title = art.find('h2').text
	article.published = art.findNext('div').text.split('By')[0].split('2010')[0] + '2010' 
	article.content = max(str(art).split('<hr />'), key=len).lstrip().split('</style>')[-1].lstrip()

	try:
		article.subtitle = art.find('h3').text
	except AttributeError:
		article.subtitle = None

	try:
		article.author = art.find('div').find('div').find('em').text.replace('By ', '')
	except AttributeError:
		pass

	return article


if __name__ == '__main__':
	for url in get_articles():
		
		page_content = get_article(url)
		article = parse_article(page_content)
		article.to_django()
		print 'Title: %s' % (article.title)
#		print '%s, by %s \n(%s)\n' % (article.title, article.author, article.subtitle)
#		print a