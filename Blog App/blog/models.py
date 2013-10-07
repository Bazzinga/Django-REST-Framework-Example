from django.db import models
 
class Author(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	birth_date = models.DateField()
	
	def __str__(self):
		return "%s %s (%s)" % (self.first_name, self.last_name, self.birth_date)
 
class Post(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField()
	author = models.ForeignKey(Author)
	body = models.TextField()
	
	def __str__(self):
		return "%s (%s)" % (self.title, self.author.last_name)