from django.db import models

# Create your models here.
class Product(models.Model):
    name_1 = models.CharField(max_length=255)
    name_2 = models.CharField(max_length=255, default="-")
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()