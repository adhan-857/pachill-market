from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_1 = models.CharField(max_length=255)
    name_2 = models.CharField(max_length=255, default="-")
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    description = models.TextField()