from django.db import models

# Create your models here.
class BWUser(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class product_data(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50) 
    base_price = models.IntegerField()
    high_price = models.IntegerField(blank=True, null=True)
    buyer_id = models.IntegerField(blank=True, null=True)
    information =  models.CharField(max_length=500)
    auction_day_left = models.IntegerField(null=True)
    product_image = models.ImageField(upload_to='images/')
    user_id = models.ForeignKey(BWUser,null=True,blank=True,on_delete=models.CASCADE)

class watchlist_data(models.Model):
    watchlist_id = models.AutoField(primary_key=True)
    watch_user_id = models.IntegerField(blank=True, null=True)
    product_id = models.ForeignKey(product_data,null=True,blank=True,on_delete=models.CASCADE)

class cart_data(models.Model):
    item_id = models.AutoField(primary_key=True)
    my_price = models.IntegerField(blank=True, null=True)
    cart_user_id = models.IntegerField(blank=True, null=True)
    product_id = models.ForeignKey(product_data,null=True,blank=True,on_delete=models.CASCADE)

class schedular_flag(models.Model):
    item_id = models.AutoField(primary_key=True)
    d = models.IntegerField(blank=True, null=True)
    m = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
