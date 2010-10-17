#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cookielib
import datetime
import os
import urllib2


from BeautifulSoup import BeautifulSoup
from dateutil.parser import parse as dtime

from django.core.management import setup_environ
#from django.db.utils import IntegrityError

from wincstar import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'wincstar.settings'
setup_environ(settings)

from wincstar.ripper.models import Article as DjangoArticle



class Article(object):
	"""An article."""

	def __init__(self):
		self.slug = None
		self.title = None
		self.subtitle = None
		self.published = None
		self.author = None
		self.content = None
		self.url = None

	def to_django(self):

		art = DjangoArticle()
		art.title = self.title
		art.subtitle = self.subtitle
		art.published = dtime(self.published)
		art.author = self.author
		art.content = self.content
		art.ourl = self.url
		art.slug = self.slug

		
		if len(self.content) > 1000:
			art.save()
		else:
			print('%s had no usable content.' % (self.title if self.title else ''))

#http://www.winchesterstar.com/pages/choose_edition/date:2010-10-03


def get_articles(url='http://www.winchesterstar.com/members/login'):
	opener = urllib2.build_opener(
			urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
	opener.addheaders.append(
			('Content-Type', 'application/x-www-form-urlencoded'))
	login_data = (
		r'_method=POST&data%5BMember%5D%5Bemail'
		r'%5D=thepythonist%40gmail.com&data%5BMember'
		r'%5D%5Bpassword%5D=UXe1b&data%5BMember%5D%5Bremember%5D=0'
	)
	opener.open('http://www.winchesterstar.com/members/login', login_data).read()

	content = opener.open(url, login_data).read()

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
	_content = max(str(art).split('<hr />'), key=len).lstrip().split('</style>')[-1].lstrip()
	article.content = BeautifulSoup(_content).prettify()


	try:
		article.subtitle = art.find('h3').text
	except AttributeError:
		article.subtitle = None

	try:
		article.author = art.find('div').find('div').find('em').text.replace('By ', '')
	except AttributeError:
		pass

	return article


def date_range(start_date):
	"""
	Returns a generator of all the days between two date objects.

	Results include the start and end dates.

	Arguments can be either datetime.datetime or date type objects.

	h3. Example usage

		>>> import datetime
		>>> import calculate
		>>> dr = calculate.date_range(datetime.date(2009,1,1), datetime.date(2009,1,3))
		>>> dr
		<generator object="object" at="at">
		>>> list(dr)
		[datetime.date(2009, 1, 1), datetime.date(2009, 1, 2), datetime.date(2009, 1, 3)]

	"""
	# If a datetime object gets passed in,
	# change it to a date so we can do comparisons.
	
	end_date = datetime.datetime.now()
	
	if isinstance(start_date, datetime.datetime):
		start_date = start_date.date()
	if isinstance(end_date, datetime.datetime):
		end_date = end_date.date()

	# Verify that the start_date comes after the end_date.
	if start_date > end_date:
		raise ValueError('You provided a start_date that comes after the end_date.')

	# Jump forward from the start_date...
	while True:
		yield start_date
		# ... one day at a time ...
		start_date = start_date + datetime.timedelta(days=1)
		# ... until you reach the end date.
		if start_date > end_date:
			break

if __name__ == '__main__':

	

	for date in date_range(datetime.datetime.now()):
		print 'Grabbing %s' % (date)
		
		for url in get_articles('http://www.winchesterstar.com/pages/choose_edition/date:%s' % date):
			
			page_content = urllib2.urlopen(url).read()
			article = parse_article(page_content)
			article.url = url

			article.slug = '%s-%s' % (date, url.split('/')[-1].replace('_', '-'))
			try:
				article.to_django()
			except:
				print '%s already exists.' % (article.title)

			print 'Grabbing: %s' % (article.title)
