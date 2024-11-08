from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products (models.Model):
    name = models.TextField()
    P_id=models.TextField()
    price =models.TextField()
    offer_price = models.TextField()
    image = models.FileField()
    description = models.TextField()
    highlights = models.TextField()
    phone=models.BooleanField(default=False)
    dress=models.BooleanField(default=False)
  


