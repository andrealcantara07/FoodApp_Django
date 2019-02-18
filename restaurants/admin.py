from django.contrib import admin
from .models import Food
from .models import OrderItem, Order, Profile
# Register your models here.

admin.site.register(Food)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Profile)
