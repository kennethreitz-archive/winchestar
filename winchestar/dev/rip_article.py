#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

from BeautifulSoup import BeautifulSoup

import models



ARTICLE_URL = 'http://www.winchesterstar.com/articles/view/firefighters_share_their_expertise_and_equipment'

# TESTING = True
TESTING = False




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