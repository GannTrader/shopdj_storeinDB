from django.db import models

# Create your models here.
class product(models.Model):
	title = models.CharField(max_length = 255)
	descript = models.TextField()
	price = models.FloatField()
	image = models.FileField()

	def __str__(self):
		return self.title


class cart(models.Model):
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.product} with quantity = {self.quantity}"