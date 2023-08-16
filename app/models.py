from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES =(
    ('ANI','andaman & nicobar islands'),
    ('andhra p', 'andhra pradesh'),
    ('arunachal p','arunachal pradesh'),
    ('ass','assam'),
    ('bih','bihar'),
    
    ('chat','chandigarah'),
    ('chandi','chhatisgarah'),
    ('dadarNagar','dadar & nagar haveli'),
    ('dlh','delhi'),
    ('goaa','goa'),
    ('guj','gujrat'),
    ('har','haryana'),
    ('him p','himachal pradesh'),
    ('J&K','jammu & kashmir'),
    ('jhar','jharkhand'),
    ('kar','karnataka'),
    ('ker','kerla'),
    ('laksh','lakshadweep'),
    ('MP','madhya pradesh'),
    ('maha','maharashtra'),
    ('Mani','manipur'),
    ('Megh','meghalay'),
    ('Mizz','mizoram'),
    ('naga','nagaland'),
    ('odi','odisha'),
    ('podu','poducherry'),
    ('pun','punjab'),
    ('rat','rajasthan'),
    ('sik','sikkim'),
    ('tam','tamil nadu'),
    ('tel','telangana'),
    ('tri','tripura'),
    ('uttra','uttrakhand'),
    ('UP','uttar pradesh'),
    ('WB','west bengal'),
 )

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length = 50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES , max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
        ('M' ,'Mobile'),
        ('L', 'Laptop'),
        ('TW', 'Top Wear'),
        ('BW', 'Bottom Wear'),
    )

class Product(models.Model):
     title = models.CharField(max_length = 100)
     selling_price = models.FloatField()
     discounted_price = models.FloatField()
     description = models.TextField()
     brand = models.CharField(max_length = 100)
     category = models.CharField(choices = CATEGORY_CHOICES, max_length = 8)
     product_image = models.ImageField(upload_to = 'productimg')

     def __str__(self):
         return str(self.id)

class Cart(models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     product = models.ForeignKey(Product, on_delete = models.CASCADE)
     quantity = models.PositiveIntegerField(default = 1)
        
     def __str__(self):
         return str(self.id)

     @property
     def total_cost(self):
       return self.quantity * self.product.discounted_price

STATUS_CHOICES =(
     ('Accepted','accepted'),
     ('Packed','packed'),
     ('OnTheWay','on the way'),
     ('Delivered','delivered'),
     ('Cancel','cancel'),
    )

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
   



# Create your models here.