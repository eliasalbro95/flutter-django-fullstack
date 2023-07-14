from rest_framework import serializers

from products.models import Maker, Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        depth = 1


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = "__all__"
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
