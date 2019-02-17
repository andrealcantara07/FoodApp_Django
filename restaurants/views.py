from django.shortcuts import render
from .models import Food, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def food(request):
    foods = Food.objects
    return render(request, 'restaurants/food.html', {'foods': foods})

def home(request):
    return render(request, 'restaurants/home.html')


'''
/--------------
 SHOPPING CART
--------------/
'''

def add_to_cart(request, **kwargs):
    food = Food.objects.filter(id=kwargs.get('item_id', '')).first()

    order_item, status = OrderItem.objects.get_or_create(food=food)

    return redirect('/food/')

def cart(request, **kwargs):
    return render(request, 'restaurants/cart.html')



'''
/--------
  ABOUT
--------/
'''