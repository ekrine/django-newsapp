from django.contrib import admin

# Register your models here.
from main.models import Article, Category

admin.site.register(Article)
admin.site.register(Category)

#Override the admin site settings
admin.site.site_header = 'News App - Admin'
admin.site.site_title = 'News App - Admin'