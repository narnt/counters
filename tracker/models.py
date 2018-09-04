from django.db import models
from django.utils import timezone

# Create your models here.
class Counter(models.Model):
	"""docstring for Counter"""
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	count = models.IntegerField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def inc(self):
		self.count = self.count+1

	def __str__(self):
		return self.title