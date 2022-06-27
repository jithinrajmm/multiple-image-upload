from django.urls import path
from images import views

urlpatterns = [
    path('',views.create_post,name = 'create_post'),
    path('sin/<int:pk>/',views.details,name='details'),
    path('edit/<int:pk>/',views.product_edit,name='edit')
]