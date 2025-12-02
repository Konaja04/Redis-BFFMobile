from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, ProductListSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').filter(is_active=True)
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'rating', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_products = self.queryset.filter(rating__gte=4.0)[:10]
        serializer = self.get_serializer(featured_products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='all')
    def all_products(self, request):
        """Devuelve TODOS los productos sin paginación"""
        products = self.queryset.all()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)