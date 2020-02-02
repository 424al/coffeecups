from django.contrib import admin
from .models import ShopInfo
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','shop_name','contact_phone')
    search_fields = ['shop_name']
    prepopulated_fields = {'slug': ('shop_name',)}

admin.site.register(ShopInfo,PostAdmin)