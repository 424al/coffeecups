from django.urls import path,include
from . import views

urlpatterns = [
   path('index/',views.index,name='blog index'),
   path('<slug:slug>/',views.blogdetail,name='blog detail'),


    
]
