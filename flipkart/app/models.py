from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products (models.Model):
    name = models.TextField()
    P_id=models.TextField()

    image = models.FileField()
    description = models.TextField()
    highlights = models.TextField()
    phone=models.BooleanField(default=False)
    dress=models.BooleanField(default=False)
    laptop=models.BooleanField(default=False)
    others=models.BooleanField(default=False)

class Categorys(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    storage=models.TextField()
    color=models.TextField()
    price =models.TextField()
    offer_price = models.TextField()
    size=models.TextField()

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)

class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
