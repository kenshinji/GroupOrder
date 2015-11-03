from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Dish

# Create your views here.
def restaurant_list(request):
    #####dummy data
    Restaurant.objects.all().delete()
    restaurant1 = Restaurant()
    restaurant1.name = "Macdonald"
    restaurant1.status = True
    restaurant1.save()
    restaurant2 = Restaurant()
    restaurant2.name = "KFC"
    restaurant2.status = False
    restaurant2.save()
    restaurants = [restaurant1, restaurant2]
    #####dummy data

    return  render(request, 'order/restaurant_list.html', {'restaurants' : restaurants})

def menu(request, pk):
    #####dummy data
    dish1 = Dish()
    dish1.name = "dish1"
    dish1.price = 10.5
    dish2 = Dish()
    dish2.name = "dish2"
    dish2.price = 20
    menu = [dish1, dish2]
    #####dummy data

    return render(request, 'order/menu.html', {'menu' :  menu})
