from django.contrib import admin
from  shop.models import  product,contact

# Register your models here.

class  products (admin.ModelAdmin):
    list_display = ['product_name',' desc','pub_date']

admin.site.register(product)
admin.site.register(contact)
