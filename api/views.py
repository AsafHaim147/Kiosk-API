from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from .models import Category,Dish

# Create your views here.
class CategoriesAll(APIView):
    def get(self,request):
        cats = Category.objects.all()
        return JsonResponse([cat.serialize() for cat in cats],safe=False)
    
class DishByCategory(APIView):
    def get(self,request,id):
        dishes = Dish.objects.filter(category_id=id)
        return JsonResponse([dish.serialize() for dish in dishes],safe=False)


