#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib

from BeautifulSoup import BeautifulSoup


username = 'thepythonist@gmail.com'
password = 'UXe1b'


opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
opener.addheaders.append(('Content-Type', 'application/x-www-form-urlencoded'))

login_data = r'_method=POST&data%5BMember%5D%5Bemail%5D=thepythonist%40gmail.com&data%5BMember%5D%5Bpassword%5D=UXe1b&data%5BMember%5D%5Bremember%5D=0'
opener.open('http://www.winchesterstar.com/members/login', login_data).read()
content = opener.open('http://www.winchesterstar.com/members/login', login_data).read()

soup = BeautifulSoup(content)

links = []

for link in [str(l['href']) for l in soup.findAll('a') if 'homepage_links' in l['href']]:
	c = opener.open('http://www.winchesterstar.com/%s' % link)
	links.append(c.geturl())
	
print links