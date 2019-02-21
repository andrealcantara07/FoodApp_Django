from __future__ import unicode_literals
from django.shortcuts import render
from .models import Food, Order, OrderItem, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
import datetime
from datetime import date
import random
import string
from django.urls import reverse
# Create your views here.

'''
/-------
  FOOD
-------/
'''
def food(request):
    foods = Food.objects
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [food.food for food in user_order_items]

    context = {
        'foods': foods,
        'current_order_products': current_order_products

    }

    return render(request, 'restaurants/food.html', context)

def home(request):
    return render(request, 'restaurants/home.html')

'''
/-------
  USER
-------/
'''
def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner= my_user_profile)
    context = {
        'my_orders': my_orders
    }

    return render(request, 'profile.html', context )

def get_user_pending_order(request):

    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)

    if order.exists():
        return order[0]
    return 0


'''
/--------------
 SHOPPING CART
--------------/
'''
def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])

def add_to_cart(request, **kwargs):

    user_profile = get_object_or_404(Profile, user=request.user)
    food = Food.objects.filter(id=kwargs.get('item_id', '')).first()

    if food in request.user.profile.food.all():
        messages.info(request, 'Passed the quantity limit')
        return redirect('food')

    order_item, status = OrderItem.objects.get_or_create(food=food)

    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)

    if status:

        user_order.ref_code = generate_order_id()
        user_order.save()

    messages.info(request, 'Item added to cart')
    return redirect('/food/')



def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect('/cart/')


def cart(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'restaurants/cart.html', context)

def checkout(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'restaurants/checkout.html', context)

def checkout(request):
    messages.info(request, 'Your order is being delivered')
    return render(request, 'restaurants/checkout.html')



'''
/--------
  ABOUT
--------/
'''