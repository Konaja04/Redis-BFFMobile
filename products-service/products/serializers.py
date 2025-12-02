from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    in_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'image_url',           # ← AGREGAR ESTE CAMPO
            'thumbnail_url',       # ← ESTE YA DEBERÍA ESTAR
            'stock', 
            'category',
            'category_name',
            'rating',
            'in_stock',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class ProductListSerializer(serializers.ModelSerializer):
    """Serializer optimizado para listados"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    in_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'price', 
            'image_url',           # ← AGREGAR ESTE CAMPO TAMBIÉN
            'thumbnail_url',
            'stock',
            'category_name',
            'rating',
            'in_stock'
        ]