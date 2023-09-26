from django.contrib import admin
from .models import*
from django.utils.html import format_html
# Register your models here.


admin.site.register(user)
admin.site.register(main_category)

class product(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display=("main_category","name","image_tag","price")
    
admin.site.register(product1,product)
admin.site.register(subcategory)
admin.site.register(contactpage)

class add(admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display=("pro_name","image_tag","price","total")
    
admin.site.register(add_to_cart,add)

admin.site.register(coupon)

class billing(admin.ModelAdmin):
    list_display=("first_name","last_name","address","email","phone")

admin.site.register(billing_detail,billing)

class order1(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display=("image_tag","product_name","qtn","product_total","total")
    
    
admin.site.register(orders,order1)

admin.site.register(brand)
admin.site.register(filter_price)
admin.site.register(color)
admin.site.register(size)

class showwishlist(admin.ModelAdmin):
    def image_tag(self,obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display=("image_tag","name","price")
    
admin.site.register(wishlist,showwishlist)