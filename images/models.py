from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    
    def __str__(self) -> str:
        return self.product.name+ str(self.product.id)