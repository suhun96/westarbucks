
from django.db import models
from django.forms import CharField

# class Menu(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta: #메타 정보 : 중요한 정보.
#         db_table = 'menus'

# class Category(models.Model):
#     name = models.CharField(max_length=20)
#     menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'categories'

# class Product(models.Model):
#     name     = models.CharField(max_length=100)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'products'

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'categories'
        
class Drink(models.Model):
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    korea_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    
    class Meta:
        db_table = 'drinks'

class Image(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'allergen'
        
class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'allergydrinks'
        
class Nutrition(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
   
    one_serving_kcal = models.DecimalField(max_digits=10,decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10,decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10,decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10,decimal_places=2)
    protein_g = models.DecimalField(max_digits=10,decimal_places=2)
    caffeine_g = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        db_table = 'nutritions'

