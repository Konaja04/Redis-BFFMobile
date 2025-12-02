import requests
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache # Importar el objeto de caché de Django

# URL del servicio de productos (apunta al contenedor de Docker o Railway)
# La variable de entorno PRODUCTS_SERVICE_URL ya se está inyectando correctamente
PRODUCTS_SERVICE_URL = os.getenv('PRODUCTS_SERVICE_URL', 'http://localhost:8001')

# El tiempo de vida de la caché (debe coincidir con settings.py)
# 5 minutos = 300 segundos
CACHE_TIMEOUT = 5 * 60 


@api_view(['GET'])
def products_list_mobile(request):
    """
    BFF Mobile: Respuestas ligeras optimizadas para mobile con caching de Redis.
    """
    page = request.GET.get('page', 1)
    page_size = 10
    
    # 1. Definir una clave de caché única basada en los parámetros de la solicitud
    cache_key = f'products_list_mobile_page_{page}'
    
    # 2. Intentar obtener la respuesta completa de la caché
    cached_response_data = cache.get(cache_key)
    
    if cached_response_data:
        # ✅ Cache Hit
        print(f"✅ Cache HIT para la clave: {cache_key}")
        return Response(cached_response_data) 

    # 3. Cache Miss: Proceder a llamar al servicio externo
    print(f"❌ Cache MISS para la clave: {cache_key}. Llamando a servicio externo...")
    try:
        response = requests.get(
            f'{PRODUCTS_SERVICE_URL}/api/products/',
            params={'page': page, 'page_size': page_size},
            timeout=5
        )
        
        if response.status_code != 200:
            return Response(
                {'error': 'Error al obtener productos del servicio externo'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        data = response.json()
        
        # Transformar los datos (Lógica BFF)
        mobile_products = []
        for product in data.get('results', []):
            mobile_products.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'thumbnail_url': product['thumbnail_url'],
                'in_stock': product['in_stock'],
                'rating': product['rating']
            })
        
        # 5. Construir el cuerpo de la respuesta final que será cacheado
        final_response_data = {
            'results': mobile_products,
            'page': page,
            'page_size': page_size,
            'source': 'BFF Mobile - Optimizado para iOS'
        }
        
        # 6. ¡GUARDAR EN REDIS!
        cache.set(cache_key, final_response_data, timeout=CACHE_TIMEOUT)
        
        return Response(final_response_data)
    
    except requests.RequestException as e:
        return Response(
            {'error': f'Error de conexión con el servicio de productos: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def product_detail_mobile(request, pk):
    """Detalle mínimo de producto para móvil con caching de Redis."""
    
    # 1. Definir una clave de caché única basada en el PK (ID del producto)
    cache_key = f'product_detail_mobile_pk_{pk}'
    
    # 2. Intentar obtener la respuesta completa de la caché
    cached_response_data = cache.get(cache_key)
    
    if cached_response_data:
        # ✅ Cache Hit
        print(f"✅ Cache HIT para la clave de detalle: {cache_key}")
        return Response(cached_response_data) 

    # 3. Cache Miss: Proceder a llamar al servicio externo
    print(f"❌ Cache MISS para la clave de detalle: {cache_key}. Llamando a servicio externo...")
    try:
        response = requests.get(f'{PRODUCTS_SERVICE_URL}/api/products/{pk}/', timeout=5)
        
        if response.status_code == 404:
            return Response(
                {'error': 'Producto no encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if response.status_code != 200:
             return Response(
                {'error': 'Error al obtener producto del servicio externo'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
        product = response.json()
        
        # Transformación de datos (Lógica BFF)
        mobile_product = {
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'thumbnail_url': product['thumbnail_url'],
            'description': product['description'][:100] + '...',  # Descripción corta
            'in_stock': product['in_stock'],
            'rating': product['rating']
        }
        
        # 4. ¡GUARDAR EN REDIS!
        cache.set(cache_key, mobile_product, timeout=CACHE_TIMEOUT)
        
        return Response(mobile_product)
    
    except requests.RequestException as e:
        return Response(
            {'error': f'Error de conexión con el servicio de productos: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )