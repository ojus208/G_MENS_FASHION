from django.contrib import admin
from .models import Offer_poster, Brand, Product_desc, Products_type, Products, category_product, Orders, Address, auth_user, images, Sizes, sizes_stock, Transaction


admin.site.register(Offer_poster)
admin.site.register(Brand)
admin.site.register(Products_type)
admin.site.register(Product_desc)
admin.site.register(category_product)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Address)
admin.site.register(auth_user)
admin.site.register(images)
admin.site.register(Sizes)
admin.site.register(sizes_stock)
admin.site.register(Transaction)

