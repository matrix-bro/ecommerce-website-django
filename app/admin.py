from django.contrib import admin
from app.models.user import User, CustomUserManager
from app.models.category import Category
from app.models.orders import Orders, ProductOrderDetail
from app.models.product import Product

admin.site.register(User)
admin.site.register(Category)
admin.site.register(ProductOrderDetail)
admin.site.register(Product)
admin.site.register(Orders)