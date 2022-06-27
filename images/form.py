from dataclasses import fields
from pyexpat import model
from tkinter import Image
from images.models import Product,Images
from django import forms



class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductEditForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image',]