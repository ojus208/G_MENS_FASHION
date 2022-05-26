from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Offer_poster(models.Model):
    sno = models.AutoField(primary_key=True)
    title =  models.CharField(max_length=600)
    poster = models.ImageField(upload_to="media")
    detail = models.TextField()

    def __str__(self):
        return self.title

class Brand(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Products_type(models.Model):
    sno = models.AutoField(primary_key=True)
    poster = models.ImageField(upload_to="media" )
    type = models.CharField(max_length=500)
    title = models.CharField(max_length=3000, default="")

    def __str__(self):
        return self.type


class category_product(models.Model):
    sno = models.AutoField(primary_key=True)
    poster = models.ImageField(upload_to="media")
    category = models.CharField(max_length=500)

    def __str__(self):
        return self.category



class Product_desc(models.Model):
    sno = models.AutoField(primary_key=True) 
    color_available = models.CharField(max_length=30000)
    desc_query = models.CharField(max_length=10000)
    desc = models.TextField()

    def __str__(self):
        return self.desc_query


class images(models.Model):
    sno = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="media")
    image_name = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.image_name

class Sizes(models.Model):
    sno = models.AutoField(primary_key=True)
    size = models.CharField(max_length=500)

    def __str__(self):
        return self.size

class sizes_stock(models.Model):
    sno = models.AutoField(primary_key=True)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    product_name = models.CharField(max_length=500, default="")

    def __str__(self):
        return f'{self.size} {self.product_name}'



class Products(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=5000)
    company = models.CharField(max_length=100, default="")
    poster = models.ImageField(upload_to="media", default="/ntg/")
    image = models.ManyToManyField(images)
    price = models.IntegerField(default=0)
    off = models.FloatField(default=0.0)
    mrp = models.FloatField(default=0)
    desc = models.ManyToManyField(Product_desc, default="")
    size = models.ManyToManyField(sizes_stock, default="")
    Product_type = models.ForeignKey(Products_type, on_delete=models.CASCADE, default="")
    category = models.ForeignKey(category_product, on_delete=models.CASCADE  , default="")
    offers = models.ForeignKey(Offer_poster, on_delete=models.CASCADE  , default="" ) 
    trending = models.BooleanField(default=False)
    demanding = models.BooleanField(default=False)
    original = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Address(models.Model):
    sno = models.AutoField(primary_key=True)
    address = models.TextField()
    contact_num = models.IntegerField()


class auth_user(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="media", default="avatar.jpg")
    phone = models.IntegerField()
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order = models.TextField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Orders(models.Model):
    items_json = models.TextField()
    products = models.ManyToManyField(Products)
    total_ammount = models.FloatField()
    deliverd = models.BooleanField(default=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    user  = models.ForeignKey(auth_user, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

    



