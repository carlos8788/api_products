from .models import ProductCategory, Products
from rest_framework import serializers


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
    
    class Meta:
        model = Products
        fields = ["name", "description", "quantity", "price", "category", 'category_name', "img_url"]



class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["name"]
