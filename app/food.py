from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *


def food_create(request):

    FoodEntry.objects.create(title=request.GET.get("food_name",""), price=request.GET.get("food_price",""))
    return redirect("/")

def food_delete(request):

    FoodEntry.objects.filter(title__iexact=request.GET.get("food_name","")).delete()
    return redirect("/")
 
def food_read(request):
  
  FoodEntryAll = FoodEntry.objects.all()

  return render(request, 'food/food_read.html',
      { 'page_active': 4,
      'res': FoodEntryAll })