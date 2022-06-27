
from tkinter import Image
from django.shortcuts import render
from images.form import ProductForms,ImagesForm,ProductEditForms
from django.http import HttpResponse
from django.forms import modelformset_factory
from images.models import Product,Images
from django.shortcuts import get_object_or_404

# Create your views here.
def create_post(request):
    
    imageFormSet = modelformset_factory(Images,fields=('image',),extra=4)
    # extra is how many forms do i need 
    
    if request.method == 'POST':
        
        form = ProductForms(request.POST or None)
        formset = imageFormSet(request.POST or None, request.FILES or None)
        
        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.save()
            
            
            for singleform in formset:
                try:
                    photo = Images(product=product,image = singleform.cleaned_data['image'])
                    photo.save()
                    
                except Exception as e:
                    print('errorrr',e)
                    break
    
    form = ProductForms()
    formset = imageFormSet(queryset=Images.objects.none())
    # ith koduthillenkil Images.objects.all() images show aakum
    context = {
        'form': form,
        'formset':formset
    }
    return render(request,'postcreate.html',context)
    
    
def details(request,pk):
    
    product = Product.objects.get(id=pk)
    images = Images.objects.filter(product = product)
    context = {
        'product': product,
        'images': images
    }
    return render(request,'detailview.html',context)
    

# author of the post want to add more images
# user need to edit the uploaded images , update
# user need to delete the posted images
def product_edit(request,pk):
    product = get_object_or_404(Product,pk=pk)
    
    imageFormSet = modelformset_factory(Images,fields=('image',),extra=4,max_num=5)
    
    
    if request.method == 'POST':
        form = ProductEditForms(request.POST,instance=product)
        formset = imageFormSet(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            form.save()
            # print(formset.cleaned_data)
            existing_images = Images.objects.filter(product=product)
            print(existing_images)
            for index,f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        product = Images(product=product,image=f.cleaned_data['image'])
                        product.save()
                        return HttpResponse('success')
                    elif f.cleaned_data['image'] is False:
                        # inspect the form you will get the form-position-id in the input hidden
                        # field
                        photo = Images.objects.get(id=request.POST.get('form-'+str(index)+'-id'))
                        photo.delete()
                        return HttpResponse('success')
                    else:
                        photo = Images(product=product,image=f.cleaned_data['image'])
                        data = Images.objects.get(id=existing_images[index].id)
                        data.image = photo.image
                        data.save()
    
                        
            
    form = ProductEditForms(instance=product)
    formset = imageFormSet(queryset=Images.objects.filter(product=product))
    context = {
        'form': form,
        'formset':formset,
        
    }
    
    return render(request,'productedit.html',context)
    
    
    

