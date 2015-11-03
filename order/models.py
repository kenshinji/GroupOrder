from django.db import models
from django.utils import timezone

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    money_left = models.FloatField()

class Dish(models.Model):
    restaurant_name = ""
    name = ""
    price = 0

class Restaurant(models.Model):
    name = ""
    status = False

class OrderStatus(models.Model):
    is_ordering = False

class OrderList(models.Model):
    restaurant = ""
    timestamp = timezone.now()
    order_dict = {}