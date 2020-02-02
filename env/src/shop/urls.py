from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('shops/', views.shopindex, name='shop index',),
    path('shops/<slug:slug>/', views.shopdetail, name='shop_info'),
    path('addshop/',views.register, name='addshop')
    
]
