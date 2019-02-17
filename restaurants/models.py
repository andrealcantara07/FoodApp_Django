from django.db import models

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
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])
