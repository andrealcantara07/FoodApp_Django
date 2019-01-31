from django.shortcuts import render
from .models import Food
# Create your views here.
def food(request):
    foods = Food.objects
    return render(request, 'restaurants/food.html', {'foods': foods})