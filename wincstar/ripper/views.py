# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse

from ripper.models import Article



def index(request):
	latest_articles = Article.objects.all().order_by('-published')
	return render_to_response('index.html', {'articles': latest_articles})


def detail(request, article_id):

	art = get_object_or_404(Article, pk=article_id)	
	return render_to_response('detail.html', {'article': art})