from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
        }
    
    class Meta:
        db_table = 'dishes_category'

class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=500)
    is_gluten_free = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = 'dishes_dish'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'is_gluten_free': self.is_gluten_free,
            'is_vegan': self.is_vegan,
            'category' : self.category.serialize()
        }
    