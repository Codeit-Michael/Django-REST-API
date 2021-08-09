from django.db import models

# Create your models here.
class employee(models.Model):
	firstname = models.CharField(max_length=15)
	lastname = models.CharField(max_length=15)
	myid = models.IntegerField()

	def __str__(self):
		return self.firstname