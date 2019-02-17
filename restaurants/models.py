from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
# Create your models here.

'''
/-------
  FOOD
-------/
'''
class Food(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    price = models.FloatField(default = 0)
    image = models.ImageField(upload_to='food_images/')

'''
/--------
  USER
--------/
'''
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food, blank=True)

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    
post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

'''
/--------------
 Shopping Cart
--------------/
 '''
class OrderItem(models.Model):
    food = models.OneToOneField(Food, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
