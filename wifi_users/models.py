from django.db import models

# Create your models here.
class Voucher(models.Model):

	code = models.CharField(max_length=50, null=True)
	quantity = models.CharField(max_length=50)
	max_device = models.CharField(max_length=50)
	voucher_format = models.CharField(max_length=50)
	length = models.CharField(max_length=50)
	duration = models.CharField(max_length=50)
	price = models.CharField(max_length=50)
	purge_after = models.CharField(max_length=50)