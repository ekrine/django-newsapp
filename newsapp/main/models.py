from django.db import models

class Category(models.Model):

	#str Helper method to return the title if we list out
	def __str__(self):
		return self.title

	title = models.TextField(max_length=200)


class Article(models.Model):
	title = models.TextField(max_length=200)
	author = models.TextField('Author')
	publication_date = models.DateTimeField('Date Published')
	category = models.ForeignKey(Category)	#foreign key
	hero_image = models.TextField('Hero Image')
	additional_image = models.TextField('Additonal Image', null=True, blank=True)
	body_text = models.TextField('Body')

	#str Helper method to return the title if we list out
	def __str__(self):
		return self.title
