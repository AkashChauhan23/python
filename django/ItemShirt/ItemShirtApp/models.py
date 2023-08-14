from django.db import models

class Size(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XLARGE = 'XL'
    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XLARGE, 'XL'),
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    fitting_type = models.CharField(max_length=50)
    imported = models.BooleanField(default=False)
    category_id = models.IntegerField()
    size=models.ManyToManyField(Size)

