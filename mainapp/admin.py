from django.contrib import admin
from .models import Blog_news, Category, Information
from tinymce.widgets import TinyMCE
from django.db import models

class Blog_newsAdmin(admin.ModelAdmin):
	fields=('title', 'publieshed_date', 'text', 'image',)

	formfield_overrides = {
			models.TextField: {'widget': TinyMCE(),},
	}

class Information_admin(admin.ModelAdmin):
	formfield_overrides = {
			models.TextField: {'widget': TinyMCE(),},
	}

#	fielsets=[""]
admin.site.register(Blog_news, Blog_newsAdmin)
admin.site.register(Category)
admin.site.register(Information, Information_admin)