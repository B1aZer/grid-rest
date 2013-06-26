from django.db import models

class Products(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    ProductName = models.CharField(max_length=100, blank=True, default='')
    UnitPrice = models.IntegerField()
    UnitsInStock = models.IntegerField()
    Discontinued = models.BooleanField(default=False)
    shop = models.ForeignKey('Shop', related_name='products')
    """
    class Meta:
        ordering = ('created',)
    """

class Shop(models.Model):
    ShopName = models.CharField(max_length=100)
    Address = models.TextField(null=True, blank=True)
    Category = models.CharField(max_length=100, default='Undefined')
    Country = models.CharField(max_length=100, blank=True)


