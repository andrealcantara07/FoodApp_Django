from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300)
    price = models.FloatField(default = 0)
    image = models.ImageField(upload_to='food_images/')

class OrderItem(models.Model):
    food = models.OneToOneField(Food, on_delete=models.SET_NULL, null=True)
