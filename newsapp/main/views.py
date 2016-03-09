from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import datetime
from .models import Article, Category

#*******************************************************
#ADMIN PLACEHOLDER to fix admin. IMPORTANT!!
def master():
	pass
#*******************************************************

#HOMEPAGE
def home(request):
	article = getRandomArticles(1).get()

	#ascending publication date, excluding articles in future
	today = datetime.now().date()
	articleList = Article.objects.filter(publication_date__lte=today).order_by('publication_date').all()		
	
	nextArticleList = getRandomArticles(4)

	context = {
		'article': article, 
		'articleList' : articleList,
		'nextArticleList' : nextArticleList,
		'meta_title' : 'News App',
		'meta_desc' : 'Welcome to News App',
		'meta_keywords' : 'django,news app'
	}
	return render(request, "main/home.html", context)

#*******************************************************
#ARTICLES
#*******************************************************
def article(request, article_id):
	article = Article.objects.get(pk=article_id)
	nextArticleList = getRandomArticles(4)

	context = {
		'article': article, 
		'nextArticleList' : nextArticleList,
		'meta_title' : article.title,
		'meta_desc' : article.title + ' - Read the full article',
		'meta_keywords' : article.title + ',django,news app'
	}

	return render(request, "main/article_full.html", context)

#*******************************************************
#COMMON TEMPLATE COMPONENTS (No direct URLs to these)
#*******************************************************
def navigation(request):
	return render(request, "main/_navigation.html")

def whattoreadnext(request):
	return render(request, "main/_whattoreadnext.html")

#*******************************************************
#UTILITIES

def getRandomArticles(count):
	#excluding articles in future
	today = datetime.now().date()
	return Article.objects.filter(publication_date__lte=today).all().order_by('?')[:count]

