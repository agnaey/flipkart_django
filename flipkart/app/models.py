from django.db import models
from django.contrib.auth.models import User
from .constants import PaymentStatus
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


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
    price =models.IntegerField()
    offer_price = models.IntegerField()
    size=models.TextField()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField()
    status=CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False,blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"),max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    # def __str__(self):
    #     return f"{self.id}-{self.name}-{self.status}"

class Buy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_adress=models.ForeignKey(Address,on_delete=models.CASCADE,null=True,blank=True)



