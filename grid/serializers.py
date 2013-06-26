from rest_framework import serializers
from grid.models import Products, Shop

class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.Field(source='shop.ShopName')
    shop_id = serializers.Field(source='shop.id')
    class Meta:
        model = Products
        fields = ('id', 'shop', 'shop_id', 'ProductName', 'UnitPrice', 'UnitsInStock', 'Discontinued')

class ShopSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Shop
        fields = ('id', 'products', 'ShopName', 'Address', 'Category', 'Country')
