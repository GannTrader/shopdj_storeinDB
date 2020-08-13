
from django.db import models
# Create your models here.
label = (
	('n', 'new'),
	('h', 'hot')
	)
class product(models.Model):
	title = models.CharField(max_length = 255)
	descript = models.TextField()
	price = models.FloatField()
	image = models.FileField()
	label = models.TextField(choices=label)

	def __str__(self):
		return self.title


class cart(models.Model):
	idsp = models.IntegerField()
	user = models.CharField(max_length=255)
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.FloatField()

	def __str__(self):
		return f"{self.product} -- {self.quantity} --- {self.user}"
