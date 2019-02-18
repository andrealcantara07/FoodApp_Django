"""foodapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import restaurants.views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'restaurants'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', restaurants.views.food, name='food'),
    path('', restaurants.views.home, name='home'),
    path('cart/', restaurants.views.cart, name='cart'),
    path('add-to-cart/<int:item_id>', restaurants.views.add_to_cart, name='add_to_cart'),
    path('item/delete/<int:item_id>', restaurants.views.delete_from_cart, name='delete_from_cart')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.FOOD_URL, document_root=settings.FOOD_ROOT)
urlpatterns += static(settings.CART_URL, document_root=settings.CART_ROOT)