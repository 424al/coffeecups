
from django.contrib import admin
from django.urls import path,include
from emails.views import email_list_signup
from shop.views import shopregister

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('newsletter/', include('newsletter.urls')),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    path('success/', email_list_signup, name='shop-register'),
    path('', include('shop.urls')),
    path('general/', include('general.urls')),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('contact.urls')),








    
]
