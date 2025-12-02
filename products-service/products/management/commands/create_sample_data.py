from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para productos'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('🗑️  Limpiando datos antiguos...')

        # Crear categorías
        electronics = Category.objects.create(
            name='Electrónica',
            description='Dispositivos electrónicos y accesorios de última generación'
        )
        clothing = Category.objects.create(
            name='Ropa',
            description='Moda y accesorios para todos los estilos'
        )
        home = Category.objects.create(
            name='Hogar',
            description='Artículos para hacer tu hogar más confortable'
        )
        sports = Category.objects.create(
            name='Deportes',
            description='Equipamiento deportivo de alta calidad'
        )
        books = Category.objects.create(
            name='Libros',
            description='Literatura y conocimiento para todos'
        )
        toys = Category.objects.create(
            name='Juguetes',
            description='Diversión para todas las edades'
        )

        self.stdout.write('📦 Creando categorías...')

        # Crear productos
        products = [
            # ELECTRÓNICA (15 productos)
            Product(
                name='iPhone 15 Pro Max',
                description='Smartphone Apple con chip A17 Pro, cámara de 48MP con zoom óptico 5x, pantalla Super Retina XDR de 6.7", titanio aeroespacial y USB-C',
                price=Decimal('1199.99'),
                image_url='https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=300',
                stock=45,
                category=electronics,
                rating=4.9
            ),
            Product(
                name='MacBook Pro M3',
                description='Laptop profesional con chip M3 Pro, pantalla Liquid Retina XDR de 14", 18GB RAM, 512GB SSD. Perfecta para creadores de contenido',
                price=Decimal('1999.99'),
                image_url='https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=300',
                stock=28,
                category=electronics,
                rating=4.9
            ),
            Product(
                name='AirPods Pro 2',
                description='Auriculares inalámbricos con cancelación activa de ruido adaptativa, audio espacial personalizado y estuche de carga MagSafe USB-C',
                price=Decimal('249.99'),
                image_url='https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=300',
                stock=120,
                category=electronics,
                rating=4.8
            ),
            Product(
                name='Samsung Galaxy S24 Ultra',
                description='Smartphone Android premium con S Pen integrado, cámara de 200MP, pantalla AMOLED 6.8" 120Hz, batería de 5000mAh',
                price=Decimal('1299.99'),
                image_url='https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=300',
                stock=35,
                category=electronics,
                rating=4.7
            ),
            Product(
                name='iPad Air M2',
                description='Tablet versátil con chip M2, pantalla Liquid Retina de 11", compatible con Apple Pencil Pro y Magic Keyboard',
                price=Decimal('599.99'),
                image_url='https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=300',
                stock=55,
                category=electronics,
                rating=4.6
            ),
            Product(
                name='Sony WH-1000XM5',
                description='Audífonos over-ear con mejor cancelación de ruido del mercado, 30 horas de batería, audio de alta resolución LDAC',
                price=Decimal('399.99'),
                image_url='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300',
                stock=67,
                category=electronics,
                rating=4.8
            ),
            Product(
                name='Apple Watch Series 9',
                description='Smartwatch con pantalla siempre activa más brillante, chip S9, detección de accidentes, ECG y monitoreo avanzado de salud',
                price=Decimal('429.99'),
                image_url='https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=300',
                stock=88,
                category=electronics,
                rating=4.7
            ),
            Product(
                name='Canon EOS R6 Mark II',
                description='Cámara mirrorless profesional de 24MP, video 4K 60fps, estabilización de 8 stops, enfoque automático preciso',
                price=Decimal('2499.99'),
                image_url='https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=300',
                stock=15,
                category=electronics,
                rating=4.9
            ),
            Product(
                name='Nintendo Switch OLED',
                description='Consola híbrida con pantalla OLED de 7", 64GB, audio mejorado, soporte ajustable y dock con puerto LAN',
                price=Decimal('349.99'),
                image_url='https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=300',
                stock=42,
                category=electronics,
                rating=4.6
            ),
            Product(
                name='DJI Mini 4 Pro',
                description='Drone ultraligero con cámara 4K/60fps, tiempo de vuelo 34min, detección de obstáculos omnidireccional, transmisión 20km',
                price=Decimal('759.99'),
                image_url='https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=300',
                stock=22,
                category=electronics,
                rating=4.8
            ),
            Product(
                name='LG OLED C3 55"',
                description='Smart TV OLED 4K con procesador α9 Gen6 AI, 120Hz, HDMI 2.1, Dolby Vision IQ, webOS 23',
                price=Decimal('1399.99'),
                image_url='https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=300',
                stock=18,
                category=electronics,
                rating=4.9
            ),
            Product(
                name='Logitech MX Master 3S',
                description='Mouse inalámbrico ergonómico para productividad, sensor 8K DPI, scroll electromagnético silencioso, hasta 3 dispositivos',
                price=Decimal('99.99'),
                image_url='https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300',
                stock=95,
                category=electronics,
                rating=4.7
            ),
            Product(
                name='Kindle Paperwhite Signature',
                description='E-reader con pantalla de 6.8", ajuste automático de luz cálida, 32GB, carga inalámbrica, resistente al agua IPX8',
                price=Decimal('189.99'),
                image_url='https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=300',
                stock=73,
                category=electronics,
                rating=4.6
            ),
            Product(
                name='GoPro HERO 12 Black',
                description='Cámara de acción 5.3K60, HDR, estabilización HyperSmooth 6.0, resistente al agua 10m, pantallas táctiles duales',
                price=Decimal('399.99'),
                image_url='https://images.unsplash.com/photo-1606503153255-59d7a26e6c49?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1606503153255-59d7a26e6c49?w=300',
                stock=38,
                category=electronics,
                rating=4.7
            ),
            Product(
                name='Bose SoundLink Revolve+',
                description='Altavoz Bluetooth portátil 360°, resistente al agua IPX4, 17 horas de batería, True360 Sound Technology',
                price=Decimal('329.99'),
                image_url='https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300',
                stock=56,
                category=electronics,
                rating=4.5
            ),

            # ROPA (15 productos)
            Product(
                name='Nike Air Max 270',
                description='Zapatillas deportivas con unidad Air Max visible, upper de malla transpirable, comodidad todo el día para uso casual y deportivo',
                price=Decimal('149.99'),
                image_url='https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300',
                stock=125,
                category=clothing,
                rating=4.6
            ),
            Product(
                name='Levi\'s 501 Original',
                description='Jeans icónicos de corte recto, mezclilla 100% algodón, cierre de botones, el jean más vendido del mundo desde 1873',
                price=Decimal('79.99'),
                image_url='https://images.unsplash.com/photo-1542272604-787c3835535d?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1542272604-787c3835535d?w=300',
                stock=200,
                category=clothing,
                rating=4.7
            ),
            Product(
                name='North Face Thermoball',
                description='Chaqueta de invierno con aislamiento sintético Thermoball Eco, resistente al agua DWR, comprimible y liviana',
                price=Decimal('229.99'),
                image_url='https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1551028719-00167b16eac5?w=300',
                stock=48,
                category=clothing,
                rating=4.8
            ),
            Product(
                name='Adidas Ultraboost 23',
                description='Zapatillas running con tecnología BOOST, upper Primeknit+, suela Continental, retorno de energía excepcional',
                price=Decimal('189.99'),
                image_url='https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=300',
                stock=87,
                category=clothing,
                rating=4.7
            ),
            Product(
                name='Polo Ralph Lauren Classic',
                description='Polo de manga corta 100% algodón piqué, corte clásico, logo bordado, disponible en múltiples colores',
                price=Decimal('89.99'),
                image_url='https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=300',
                stock=156,
                category=clothing,
                rating=4.5
            ),
            Product(
                name='Columbia Bugaboo Interchange',
                description='Chaqueta 3 en 1 con capa exterior impermeable y forro térmico desmontable, perfecta para clima variable',
                price=Decimal('199.99'),
                image_url='https://images.unsplash.com/photo-1544923246-77e32d0d0853?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1544923246-77e32d0d0853?w=300',
                stock=34,
                category=clothing,
                rating=4.6
            ),
            Product(
                name='Tommy Hilfiger Denim Jacket',
                description='Chaqueta de mezclilla clásica, fit regular, 100% algodón, logo signature en el pecho, estilo atemporal',
                price=Decimal('129.99'),
                image_url='https://images.unsplash.com/photo-1551537482-f2075a1d41f2?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1551537482-f2075a1d41f2?w=300',
                stock=72,
                category=clothing,
                rating=4.4
            ),
            Product(
                name='Vans Old Skool',
                description='Zapatillas skate icónicas con línea lateral, lona y gamuza, suela waffle, comodidad y estilo desde 1977',
                price=Decimal('69.99'),
                image_url='https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=300',
                stock=188,
                category=clothing,
                rating=4.6
            ),
            Product(
                name='Patagonia Better Sweater',
                description='Chaqueta fleece de poliéster reciclado, acabado resistente al agua, puños y dobladillo elásticos, calidez sostenible',
                price=Decimal('139.99'),
                image_url='https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=300',
                stock=61,
                category=clothing,
                rating=4.8
            ),
            Product(
                name='Calvin Klein Boxer Briefs Pack',
                description='Pack de 3 bóxers de algodón elástico con cinturilla icónica, suaves, cómodos y duraderos para uso diario',
                price=Decimal('42.99'),
                image_url='https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=300',
                stock=245,
                category=clothing,
                rating=4.5
            ),
            Product(
                name='Ray-Ban Wayfarer Classic',
                description='Lentes de sol icónicos con armazón acetato, lentes de cristal G-15, protección UV 100%, estilo intemporal',
                price=Decimal('153.99'),
                image_url='https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=300',
                stock=98,
                category=clothing,
                rating=4.7
            ),
            Product(
                name='Converse Chuck Taylor All Star',
                description='Zapatillas de lona clásicas high-top, suela de goma vulcanizada, parche de tobillo signature, ícono desde 1917',
                price=Decimal('59.99'),
                image_url='https://images.unsplash.com/photo-1514989940723-e8e51635b782?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1514989940723-e8e51635b782?w=300',
                stock=215,
                category=clothing,
                rating=4.6
            ),
            Product(
                name='Under Armour Tech 2.0',
                description='Camiseta deportiva con tecnología anti-olor, tejido ultra-suave y transpirable, secado rápido, ideal para entrenar',
                price=Decimal('27.99'),
                image_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=300',
                stock=178,
                category=clothing,
                rating=4.5
            ),
            Product(
                name='Timberland 6-Inch Premium',
                description='Botas impermeables de cuero nubuck, plantilla anti-fatiga, suela de goma, clásico duradero para todas las condiciones',
                price=Decimal('198.99'),
                image_url='https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=300',
                stock=54,
                category=clothing,
                rating=4.8
            ),
            Product(
                name='H&M Organic Cotton T-Shirt',
                description='Camiseta básica de algodón orgánico 100%, corte regular, suave y transpirable, producción sostenible',
                price=Decimal('12.99'),
                image_url='https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=300',
                stock=342,
                category=clothing,
                rating=4.3
            ),

            # HOGAR (12 productos)
            Product(
                name='Nespresso Vertuo Next',
                description='Cafetera de cápsulas con tecnología Centrifusion, 5 tamaños de taza, conectividad Bluetooth, reciclaje sostenible',
                price=Decimal('179.99'),
                image_url='https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=300',
                stock=68,
                category=home,
                rating=4.5
            ),
            Product(
                name='iRobot Roomba j7+',
                description='Aspiradora robot con vaciado automático, evita obstáculos con IA, mapeo inteligente, control por app y voz',
                price=Decimal('799.99'),
                image_url='https://images.unsplash.com/photo-1558317374-067fb5f30001?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1558317374-067fb5f30001?w=300',
                stock=29,
                category=home,
                rating=4.7
            ),
            Product(
                name='Dyson V15 Detect',
                description='Aspiradora inalámbrica con láser que revela polvo invisible, sensor de partículas, 60min de autonomía, filtración HEPA',
                price=Decimal('749.99'),
                image_url='https://images.unsplash.com/photo-1558317374-067fb5f30001?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1558317374-067fb5f30001?w=300',
                stock=35,
                category=home,
                rating=4.8
            ),
            Product(
                name='Instant Pot Duo Crisp',
                description='Olla multifunción 11 en 1: olla a presión, freidora de aire, vaporera, yogurtera, más. Capacidad 8L',
                price=Decimal('149.99'),
                image_url='https://images.unsplash.com/photo-1585515320310-259814833e62?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1585515320310-259814833e62?w=300',
                stock=83,
                category=home,
                rating=4.6
            ),
            Product(
                name='Philips Hue Starter Kit',
                description='Kit de iluminación inteligente con 3 bombillos LED color + puente, control por app, 16 millones de colores',
                price=Decimal('199.99'),
                image_url='https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300',
                stock=115,
                category=home,
                rating=4.7
            ),
            Product(
                name='KitchenAid Artisan Mixer',
                description='Batidora de pie 5L con 10 velocidades, motor de alto torque, bowl de acero inoxidable, 3 accesorios incluidos',
                price=Decimal('429.99'),
                image_url='https://images.unsplash.com/photo-1578643463396-0997cb5328c1?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1578643463396-0997cb5328c1?w=300',
                stock=42,
                category=home,
                rating=4.9
            ),
            Product(
                name='Breville Smart Oven Air',
                description='Horno eléctrico multifunción con freidora de aire, 13 funciones, interior de 0.8 pies³, convección Element IQ',
                price=Decimal('399.99'),
                image_url='https://images.unsplash.com/photo-1585421514738-01798e348b17?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1585421514738-01798e348b17?w=300',
                stock=31,
                category=home,
                rating=4.8
            ),
            Product(
                name='Nest Learning Thermostat',
                description='Termostato inteligente que aprende tus preferencias, control remoto, ahorro de energía certificado Energy Star',
                price=Decimal('249.99'),
                image_url='https://images.unsplash.com/photo-1545259742-24e79a0ed9ad?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1545259742-24e79a0ed9ad?w=300',
                stock=67,
                category=home,
                rating=4.6
            ),
            Product(
                name='Shark Ninja Air Fryer',
                description='Freidora de aire 6L con 6 funciones de cocción, tecnología de circulación rápida, cesta antiadherente desmontable',
                price=Decimal('129.99'),
                image_url='https://images.unsplash.com/photo-1585515320310-259814833e62?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1585515320310-259814833e62?w=300',
                stock=94,
                category=home,
                rating=4.5
            ),
            Product(
                name='Casper Original Mattress',
                description='Colchón de espuma memory foam con 3 capas, soporte zonal, certificado CertiPUR-US, garantía 10 años',
                price=Decimal('895.00'),
                image_url='https://images.unsplash.com/photo-1505693314120-0d443867891c?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1505693314120-0d443867891c?w=300',
                stock=23,
                category=home,
                rating=4.7
            ),
            Product(
                name='Le Creuset Dutch Oven 5.5L',
                description='Olla de hierro fundido esmaltado, distribución uniforme de calor, apta para horno hasta 260°C, dura toda la vida',
                price=Decimal('379.99'),
                image_url='https://images.unsplash.com/photo-1584990347449-39b6aa0d8f53?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1584990347449-39b6aa0d8f53?w=300',
                stock=38,
                category=home,
                rating=4.9
            ),
            Product(
                name='Ring Video Doorbell Pro 2',
                description='Timbre inteligente con video HD+ 1536p, detección de movimiento 3D, visión nocturna color, conversación bidireccional',
                price=Decimal('249.99'),
                image_url='https://images.unsplash.com/photo-1558002038-1055907df827?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1558002038-1055907df827?w=300',
                stock=102,
                category=home,
                rating=4.6
            ),

            # DEPORTES (10 productos)
            Product(
                name='Peloton Bike+',
                description='Bicicleta estática inteligente con pantalla táctil giratoria 24", resistencia automática, clases en vivo y on-demand',
                price=Decimal('2495.00'),
                image_url='https://images.unsplash.com/photo-1538805060514-97d9cc17730c?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1538805060514-97d9cc17730c?w=300',
                stock=12,
                category=sports,
                rating=4.8
            ),
            Product(
                name='Bowflex SelectTech 552',
                description='Mancuernas ajustables 2.5-24kg por unidad, sistema de selección rápida, reemplaza 15 sets de pesas, ahorra espacio',
                price=Decimal('549.99'),
                image_url='https://images.unsplash.com/photo-1517963879433-6ad2b056d712?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1517963879433-6ad2b056d712?w=300',
                stock=28,
                category=sports,
                rating=4.7
            ),
            Product(
                name='Trek Marlin 7',
                description='Bicicleta de montaña con cuadro Alpha Gold Aluminum, suspensión RockShox, cambios Shimano Deore, frenos hidráulicos',
                price=Decimal('1099.99'),
                image_url='https://images.unsplash.com/photo-1576435728678-68d0fbf94e91?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1576435728678-68d0fbf94e91?w=300',
                stock=19,
                category=sports,
                rating=4.8
            ),
            Product(
                name='Wilson Pro Staff RF97',
                description='Raqueta de tenis profesional 340g, patrón de encordado 16x19, headsize 97 pulg², precisión y control elite',
                price=Decimal('229.99'),
                image_url='https://images.unsplash.com/photo-1622163642998-1ea32b0bbc67?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1622163642998-1ea32b0bbc67?w=300',
                stock=44,
                category=sports,
                rating=4.6
            ),
            Product(
                name='Garmin Forerunner 265',
                description='Reloj GPS running con pantalla AMOLED, métricas avanzadas de running, training readiness, batería 13 días',
                price=Decimal('449.99'),
                image_url='https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=300',
                stock=56,
                category=sports,
                rating=4.7
            ),
            Product(
                name='Hydro Flask 40oz',
                description='Botella de acero inoxidable con aislamiento al vacío TempShield, mantiene frío 24h/caliente 12h, tapa flex',
                price=Decimal('49.95'),
                image_url='https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=300',
                stock=188,
                category=sports,
                rating=4.8
            ),
            Product(
                name='TRX Pro4 System',
                description='Sistema de entrenamiento en suspensión profesional, correas ajustables, anclaje incluido, entrena todo el cuerpo',
                price=Decimal('199.95'),
                image_url='https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=300',
                stock=72,
                category=sports,
                rating=4.6
            ),
            Product(
                name='Spalding NBA Official Ball',
                description='Balón de basketball oficial de la NBA, cuero compuesto de grano profundo, control y agarre superiores',
                price=Decimal('149.99'),
                image_url='https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1546519638-68e109498ffc?w=300',
                stock=95,
                category=sports,
                rating=4.7
            ),
            Product(
                name='Manduka PRO Yoga Mat',
                description='Tapete de yoga profesional 6mm, superficie antideslizante, ultra-denso, garantía de por vida, eco-friendly',
                price=Decimal('120.00'),
                image_url='https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=300',
                stock=84,
                category=sports,
                rating=4.8
            ),
            Product(
                name='Osprey Atmos AG 65',
                description='Mochila de trekking 65L con sistema de suspensión Anti-Gravity, panel trasero ventilado, compartimentos organizados',
                price=Decimal('289.95'),
                image_url='https://images.unsplash.com/photo-1622260614153-03223fb72052?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1622260614153-03223fb72052?w=300',
                stock=37,
                category=sports,
                rating=4.9
            ),

            # LIBROS (8 productos)
            Product(
                name='Atomic Habits - James Clear',
                description='Guía práctica para crear buenos hábitos y romper los malos mediante pequeños cambios que producen resultados extraordinarios',
                price=Decimal('16.99'),
                image_url='https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=300',
                stock=142,
                category=books,
                rating=4.9
            ),
            Product(
                name='Sapiens - Yuval Noah Harari',
                description='Historia de la humanidad desde la Edad de Piedra hasta la era moderna, explorando cómo el Homo sapiens dominó el mundo',
                price=Decimal('18.99'),
                image_url='https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=300',
                stock=98,
                category=books,
                rating=4.8
            ),
            Product(
                name='The Psychology of Money',
                description='Morgan Housel explora la relación compleja entre psicología y finanzas personales con 19 historias reveladoras',
                price=Decimal('15.99'),
                image_url='https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=300',
                stock=167,
                category=books,
                rating=4.7
            ),
            Product(
                name='Clean Code - Robert Martin',
                description='Manual esencial sobre cómo escribir código limpio, mantenible y profesional. Lectura obligada para programadores',
                price=Decimal('42.99'),
                image_url='https://images.unsplash.com/photo-1532012197267-da84d127e765?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1532012197267-da84d127e765?w=300',
                stock=73,
                category=books,
                rating=4.8
            ),
            Product(
                name='Dune - Frank Herbert',
                description='Épica de ciencia ficción sobre política, religión y ecología en el desértico planeta Arrakis. Obra maestra del género',
                price=Decimal('14.99'),
                image_url='https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=300',
                stock=134,
                category=books,
                rating=4.9
            ),
            Product(
                name='The Lean Startup - Eric Ries',
                description='Metodología revolucionaria para crear empresas y productos innovadores mediante experimentación validada y aprendizaje iterativo',
                price=Decimal('19.99'),
                image_url='https://images.unsplash.com/photo-1553729459-efe14ef6055d?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1553729459-efe14ef6055d?w=300',
                stock=89,
                category=books,
                rating=4.6
            ),
            Product(
                name='Thinking, Fast and Slow',
                description='Daniel Kahneman explora los dos sistemas de pensamiento que moldean nuestras decisiones y juicios. Premio Nobel',
                price=Decimal('17.99'),
                image_url='https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=300',
                stock=112,
                category=books,
                rating=4.7
            ),
            Product(
                name='The Hobbit - J.R.R. Tolkien',
                description='La aventura de Bilbo Bolsón que precede El Señor de los Anillos. Fantasía clásica para todas las edades',
                price=Decimal('13.99'),
                image_url='https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=300',
                stock=156,
                category=books,
                rating=4.9
            ),

            # JUGUETES (8 productos)
            Product(
                name='LEGO Star Wars Millennium Falcon',
                description='Set de construcción 7541 piezas, réplica detallada del Halcón Milenario, incluye 7 minifiguras, 84cm de largo',
                price=Decimal('849.99'),
                image_url='https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=300',
                stock=18,
                category=toys,
                rating=4.9
            ),
            Product(
                name='Nintendo Switch Mario Kart 8',
                description='Juego de carreras arcade con 48 pistas, 42 personajes, multijugador local y online hasta 12 jugadores',
                price=Decimal('59.99'),
                image_url='https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=300',
                stock=178,
                category=toys,
                rating=4.8
            ),
            Product(
                name='Barbie DreamHouse',
                description='Casa de muñecas de 3 pisos con 8 habitaciones, ascensor funcional, tobogán de piscina, 75+ accesorios incluidos',
                price=Decimal('199.99'),
                image_url='https://images.unsplash.com/photo-1566694271453-390536dd1f0d?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1566694271453-390536dd1f0d?w=300',
                stock=42,
                category=toys,
                rating=4.7
            ),
            Product(
                name='Hot Wheels Track Builder',
                description='Set de pista con looping vertical, lanzador motorizado, 2 autos incluidos, compatible con otras pistas Hot Wheels',
                price=Decimal('49.99'),
                image_url='https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300',
                stock=95,
                category=toys,
                rating=4.5
            ),
            Product(
                name='Nerf Elite 2.0 Commander',
                description='Lanzador de dardos motorizado con tambor de 6 dardos, alcance de 27m, incluye 12 dardos oficiales Nerf',
                price=Decimal('29.99'),
                image_url='https://images.unsplash.com/photo-1544498736-d0a2a2f7f7cd?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1544498736-d0a2a2f7f7cd?w=300',
                stock=132,
                category=toys,
                rating=4.6
            ),
            Product(
                name='Melissa & Doug Wooden Puzzle',
                description='Rompecabezas de madera 48 piezas para niños 4+, ilustraciones coloridas, piezas gruesas fáciles de agarrar',
                price=Decimal('14.99'),
                image_url='https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=300',
                stock=167,
                category=toys,
                rating=4.7
            ),
            Product(
                name='Play-Doh Super Color Pack',
                description='Pack de 20 botes de plastilina no tóxica en colores vibrantes, fomenta la creatividad, seguro para niños 2+',
                price=Decimal('19.99'),
                image_url='https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=300',
                stock=215,
                category=toys,
                rating=4.8
            ),
            Product(
                name='Fisher-Price Laugh & Learn Smart Stages',
                description='Juguete educativo interactivo con 3 niveles de aprendizaje, enseña números, colores, formas, canciones y frases',
                price=Decimal('34.99'),
                image_url='https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=800',
                thumbnail_url='https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=300',
                stock=88,
                category=toys,
                rating=4.6
            ),
        ]

        Product.objects.bulk_create(products)

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Creados 6 categorías y {len(products)} productos exitosamente!'
            )
        )