from django.db import models

# Create your models here.

class user(models.Model):
    image=models.ImageField(upload_to='photo',blank=True,null=True)
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(unique=True,max_length=50)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=123)
    
    def __str__(self):
        return self.email
    
class main_category(models.Model):
    image=models.ImageField(default='man-3.jpg',upload_to='photo')
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class subcategory(models.Model):
    main_category=models.ForeignKey(main_category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class brand(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class filter_price(models.Model):
    price_range=models.CharField(max_length=50)
    
    def __str__(self):
        return self.price_range
    
class color(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class size(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class product1(models.Model):
    main_category=models.ForeignKey(main_category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE,default=1)
    brand=models.ForeignKey(brand,on_delete=models.CASCADE,default=1)
    filter_price=models.ForeignKey(filter_price,on_delete=models.CASCADE,default=1)
    color=models.ForeignKey(color,on_delete=models.CASCADE,default=1)
    size=models.ForeignKey(size,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='photo')
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qtn=models.IntegerField()
    
    def __str__(self):
        return self.name
    

    
class contactpage(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    msg=models.TextField(max_length=50)
    
    def __str__(self):
        return self.name
    
class add_to_cart(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    product_id=models.ForeignKey(product1,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='photo')
    pro_name=models.CharField(max_length=20)
    price=models.IntegerField()
    qtn=models.IntegerField()
    total=models.IntegerField()
    
    def __str__(self):
        return self.pro_name
    

class coupon(models.Model):
    code=models.CharField(unique=True,max_length=10)
    discount_amount=models.IntegerField()
    min_order_amount=models.IntegerField()
    max_order_amount=models.IntegerField()
    expiry_date=models.DateTimeField()
    
    def __str__(self):
        return self.code
# model inside:
# coupan code ,
# coupan discount , discount range ,expiry date 
    
  
class billing_detail(models.Model):
    uid=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    first_name=models.CharField(max_length=20)  
    last_name=models.CharField(max_length=20)  
    contry=models.CharField(max_length=20)
    address=models.TextField(max_length=20)
    pincode=models.CharField(max_length=6)
    city=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    
    def __str__(self):
        return self.first_name
    
class orders(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    billing_id=models.ForeignKey(billing_detail,on_delete=models.CASCADE,blank=True,null=True)
    order_id=models.CharField(max_length=30,blank=True,null=True)
    image=models.ImageField()
    product_name=models.CharField(max_length=30)
    price=models.IntegerField()
    qtn=models.IntegerField()
    product_total=models.IntegerField()
    total=models.IntegerField()
    datetime=models.DateTimeField(auto_now=True,blank=True,null=True)
    
    def __str__(self):
        return self.product_name
    
      
class wishlist(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    product_id=models.ForeignKey(product1,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField()
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name   
    
    

    
    
    
    
    