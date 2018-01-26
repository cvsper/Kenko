from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Carepro(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carepro')
	name = models.CharField(max_length=500)
	number = models.CharField(max_length=500)
	avatar = models.ImageField(upload_to='carepro_img', blank=False)
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Caregiver(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='caregiver')
	name = models.CharField(max_length=500)
	number = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	avatar = models.ImageField(upload_to='caregiver_img', blank=False)

	def __str__(self):
		return self.user.get_full_name()


class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
	name = models.CharField(max_length=500)
	number = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	avatar = models.CharField(max_length=500)

	def __str__(self):
		return self.user.get_full_name()


class Care(models.Model):
	carepro = models.ForeignKey(Carepro, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	short_desc = models.CharField(max_length=500)
	image = models.ImageField(upload_to='care_img/', blank=False)
	price = models.IntegerField(default=20)

	def __str__(self):
		return self.name

class Order(models.Model):
	READY = 1
	ONTHEWAY = 2
	ARRIVED = 3

	STATUS_CHOICES = (
		(READY, 'Ready'),
		(ONTHEWAY, 'On the way'),
		(ARRIVED, 'Arrived'),
		)		

	customer = models.ForeignKey(Customer, 'on_delete')
	carepro =  models.ForeignKey(Carepro, 'on_delete')
	caregiver = models.ForeignKey(Caregiver, 'on_delete')
	address = models.CharField(max_length = 500)
	total = models.IntegerField()
	status = models.IntegerField(choices = STATUS_CHOICES)
	created_at = models.DateTimeField(default = timezone.now)
	picked_at = models.DateTimeField(blank = True, null = True)

	def __str__(self):
		return str(self.id)

class OrderDetails(models.Model):
	order = models.ForeignKey(Order, 'on_delete', related_name = 'order_details')
	care = models.ForeignKey(Care, 'on_delete')
	quantity = models.IntegerField()
	sub_total = models.IntegerField()

	def __str__(self):
		return str(self.id)