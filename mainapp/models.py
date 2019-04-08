from django.db import models

class Category(models.Model):
	categories_name = models.CharField(max_length=50, null=False)
	categories_summary = models.CharField(max_length=200)
	urls_slung_category = models.CharField(max_length=30, null=False)


	def __str__(self):
		return ("Category: %s"%(self.categories_name))

class Information(models.Model):
	title = models.CharField(max_length=200, null=False)
	text = models.TextField(null=False)
	image = models.ImageField(upload_to='img/', blank=True, null=True)
	news_catagory = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
	urls_slung_inf = models.CharField(max_length=30, null=False, default="default")

	def __str__(self):
		return ("Post tittle: %s"%(self.title))


class Blog_news(models.Model):
	title = models.CharField(max_length=200, null=False)
	text = models.TextField(null=False)
	date = models.DateTimeField(auto_now=True, null=False)
	publieshed_date = models.DateTimeField('date publieshed', null=True, blank=True)
	image = models.ImageField(upload_to='img/', blank=True, null=True)
	urls_slung = models.CharField(max_length=30, null=False, default="new_news")

	def publiesh(self):
		self.publieshed_date = datetime.now()
		self.save()

	def __str__(self):
		return ("Post tittle: %s"%(self.title))
