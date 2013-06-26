from rest_framework import serializers
from grid.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'ProductName', 'UnitPrice', 'UnitsInStock', 'Discontinued')

