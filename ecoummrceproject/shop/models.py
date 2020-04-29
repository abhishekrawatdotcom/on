from django.db import models

# Create your models here.
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desce=models.CharField(max_length=500,default='')
    desc=models.CharField(max_length=500)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/image', default="")
    
    def __str__(self):
        return self.product_name


class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name

