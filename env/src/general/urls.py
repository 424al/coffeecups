from django.urls import path,include
from . import views

urlpatterns = [
    path('contact/',views.info, name='info'),
    path('about/',views.about, name='about'),

    
]
