from django.db import models
import uuid
from app.models.product import Product
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator

class Orders(models.Model):    
    product = models.ManyToManyField(Product,
                                     through='ProductOrderDetail',
                                     through_fields=('order', 'product'),
                                     related_name="orders")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(default=timezone.now)
    # shipped date, shipper id
    

    def __str__(self):
        return self.ordered_date
    

class ProductOrderDetail(models.Model):    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField(validators=[MinValueValidator(0)])
    status = models.BooleanField(default=False)
    # discount
    
    class Meta:
        db_table = "product_order_detail"
        verbose_name = "ProductOrderDetail"
        verbose_name_plural = "ProductOrderDetails"

    def __str__(self):
        return f"{self.product.name} -> {self.order.user.first_name}"