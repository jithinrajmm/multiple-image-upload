from tkinter import Image
from django.contrib import admin
from images.models import Product,Images

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','created','updated')  
    
    
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id','product','image')  
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
