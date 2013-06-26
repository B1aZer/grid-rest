from django.db import models

class Products(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    ProductName = models.CharField(max_length=100, blank=True, default='')
    UnitPrice = models.IntegerField()
    UnitsInStock = models.IntegerField()
    Discontinued = models.BooleanField(default=False)
    """
    class Meta:
        ordering = ('created',)
    """

