#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

from BeautifulSoup import BeautifulSoup
# from lxml.html.soupparser import fromstring
import lxml.html

import models


# ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/frederick_household_incomes_shrinking'
ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/trial_beginsin_murder_committed_8_years_ago'
# TESTING = True
TESTING = False


def get_article(url):
	"""Fetches article."""
	
	if TESTING:
		fname = url.split('/')[-1]
		with open('./samples/%s' % (fname,), 'r') as f:
			return f.read()
	else:
		return urllib.urlopen(url).read()
		
	
		
def parse_article(content):
	"""Returns article object from given article content."""
	
	article = models.Article()
	
	soup = BeautifulSoup(content)
	
	# print dir(soup)
	article = max(soup.findAll('td'), key=len)
	# print article
	
	# root = lxml.html.fromstring(content)
	#	 
	#	 article.title = root.cssselect('#ArticleDetails h2')[0].text
	article.title = article.find('h2').text
	article.subtitle = article.find('h3').text
	#	 article.subtitle = root.cssselect('#ArticleDetails h3')[0].text
	# 
	#	 _author = root.cssselect('#ArticleDetails div em')[0].text
	_author = article.find('div').find('div').find('em').text
	article.author = _author.replace('By ', '')
	article.published = article.findNext('div').text.split('By')[0]

	article.content = max(str(article).split('<hr />'), key=len).lstrip()
	
	#	 
	#	 _content = root.cssselect('#ArticleDetails tr td')[0].text_content().split('	 ')
	#	 _content = [l for l in _content if len(l) > 50][0]
	#	 _content = _content.replace('.', '. ')
	#	 article.content = _content
	#	 
	#	 article.publisher = root.cssselect('#ArticleDetails div')[2].text
	#	 article.published = root.cssselect('#ArticleDetails div')[0].text.lstrip()

	return article


def main():
	page_content = get_article(ARTICLE_URL)
	article = parse_article(page_content)

	print '%s, by %s of %s \n(%s)\n' % (article.title, article.author, article.publisher, article.subtitle)

	print article.published
	print article.content


if __name__ == '__main__':
	main()