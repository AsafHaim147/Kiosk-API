from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.CategoriesAll.as_view()),
    path('categories/<int:id>',views.DishByCategory.as_view()),
]