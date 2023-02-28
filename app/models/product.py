from django.db import models
from app.models.category import Category
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    image = models.ImageField(default='default.jpg', upload_to='products/%Y%m%d/')
    inventory = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name