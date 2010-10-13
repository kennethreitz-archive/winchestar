#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

from BeautifulSoup import BeautifulSoup
# from lxml.html.soupparser import fromstring
import lxml.html

import models


# ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/frederick_household_incomes_shrinking'
# ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/trial_beginsin_murder_committed_8_years_ago'


# ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/josephine_city_a_beacon_of_hope'

# ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/oscar_not_forgotten'

ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/firefighters_share_their_expertise_and_equipment'

# TESTING = True
TESTING = False


def get_article(url):
	"""Fetches article."""
	
	if TESTING:
		fname = url.split('/')[-1]
		with open('./samples/%s' % (fname,), 'r') as f:
			return f.read()
	else:
		
		return urllib2.urlopen(url).read()
		
	
		
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
	try:
		article.subtitle = article.find('h3').text
	except AttributeError:
		article.subtitle = None
	
	#	 article.subtitle = root.cssselect('#ArticleDetails h3')[0].text
	# 
	#	 _author = root.cssselect('#ArticleDetails div em')[0].text
	try:
		article.author = article.find('div').find('div').find('em').text.replace('By ', '')
	except AttributeError:
		article.author = None
	
	article.published = article.findNext('div').text.split('By')[0]

	
	_content = max(str(article).split('<hr />'), key=len).lstrip()
	article.content = _content.split('</style>')[-1].lstrip()
	
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
	aa = [
		'http://www.winchesterstar.com/articles/view/as_foreclosures_mount_so_do_faulty_evictions', 
		'http://www.winchesterstar.com/articles/view/electric_start', 
		'http://www.winchesterstar.com/articles/view/explaining_the_process', 
		'http://www.winchesterstar.com/articles/view/proposed_amendment_for_wellness_center_could_prove_costly', 
		'http://www.winchesterstar.com/articles/view/council_oks_youth_center', 
		'http://www.winchesterstar.com/articles/view/accused_in_belk_robbery_get_bond', 
		'http://www.winchesterstar.com/articles/view/fema_delivers_snowstorm_relief_for_city_and_counties', 
		'http://www.winchesterstar.com/articles/view/middletown_raises_tax_on_lodging_meals', 
		'http://www.winchesterstar.com/articles/view/canine_co_pilot', 
		'http://www.winchesterstar.com/articles/view/standing_tall_and_proud', 
		'http://www.winchesterstar.com/articles/view/2010_bazaar_guide', 
		'http://www.winchesterstar.com/articles/view/organizations', 
		'http://www.winchesterstar.com/articles/view/handley_knocks_off_wood', 
		'http://www.winchesterstar.com/articles/view/peaking_at_the_right_time', 
		'http://www.winchesterstar.com/articles/view/rearv1iew_mirror_by_robert_stocks_business_of_baseball', 
		'http://www.winchesterstar.com/articles/view/area_briefs', 
		'http://www.winchesterstar.com/articles/view/our_view_is_that_all_there_is', 
		'http://www.winchesterstar.com/articles/view/our_view_insult_to_injury', 
		'http://www.winchesterstar.com/articles/view/open_forum_volunteer_families', 
		'http://www.winchesterstar.com/articles/view/political_cartoon'
	]
	
	for a in aa:
		# page_content = get_article(ARTICLE_URL)
		page_content = get_article(a)
		
		print len(page_content)
		try:
			article = parse_article(page_content)
		except Exception, e:
			pass
		

		print '%s, by %s \n(%s)\n' % (article.title, article.author, article.subtitle)
		print a

			# print article.published
		# print article.content


if __name__ == '__main__':
	main()