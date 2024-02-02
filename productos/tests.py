from django.test import TestCase
from .models import *


categorias = [
    {"name": "Electrónica"},
    {"name": "Ropa"},
    {"name": "Hogar"},
    {"name": "Jardinería"},
    {"name": "Deportes"},
    {"name": "Libros"},
    {"name": "Juegos"},
    {"name": "Alimentos"},
    {"name": "Belleza"},
    {"name": "Herramientas"},
]

productos = [
    {
        "name": "Smartphone XYZ",
        "description": "Última generación con 128GB",
        "quantity": 50,
        "price": 899.99,
        
    },
    {
        "name": "Camiseta algodón",
        "description": "Camiseta de algodón orgánico",
        "quantity": 100,
        "price": 19.99,
        
    },
    {
        "name": "Sofá reclinable",
        "description": "Sofá de cuero con reclinación eléctrica",
        "quantity": 10,
        "price": 499.99,
        
    },
    {
        "name": "Tijeras de podar",
        "description": "Tijeras profesionales para jardinería",
        "quantity": 30,
        "price": 29.99,
        
    },
    {
        "name": "Balón de fútbol",
        "description": "Balón oficial de tamaño y peso reglamentario",
        "quantity": 40,
        "price": 24.99,
        
    },
    {
        "name": "Novela de misterio",
        "description": "Novela de misterio y suspenso best-seller",
        "quantity": 75,
        "price": 9.99,
        
    },
    {
        "name": "Videojuego de acción",
        "description": "Videojuego de acción y aventura para consola",
        "quantity": 60,
        "price": 59.99,
        
    },
    {
        "name": "Pack de snacks orgánicos",
        "description": "Pack de 20 snacks orgánicos y saludables",
        "quantity": 200,
        "price": 29.99,
        
    },
    {
        "name": "Kit de maquillaje",
        "description": "Kit de maquillaje profesional completo",
        "quantity": 45,
        "price": 79.99,
        
    },
    {
        "name": "Taladro inalámbrico",
        "description": "Taladro inalámbrico 20V con batería de larga duración",
        "quantity": 25,
        "price": 119.99,
        
    },
    {
        "name": "Audífonos inalámbricos",
        "description": "Audífonos Bluetooth 5.0 con cancelación de ruido",
        "quantity": 80,
        "price": 59.99,
        
    },
    {
        "name": "Chaqueta impermeable",
        "description": "Chaqueta ligera y resistente al agua para todas las estaciones",
        "quantity": 70,
        "price": 49.99,
        
    },
    {
        "name": "Robot aspirador",
        "description": "Robot aspirador inteligente con mapeo de habitaciones",
        "quantity": 25,
        "price": 299.99,
        
    },
    {
        "name": "Maceta autoregable",
        "description": "Maceta inteligente con sistema de auto riego",
        "quantity": 50,
        "price": 34.99,
        
    },
    {
        "name": "Zapatillas de running",
        "description": "Zapatillas deportivas con amortiguación y soporte",
        "quantity": 60,
        "price": 89.99,
        
    },
    {
        "name": "Guía de viajes",
        "description": "Guía de viajes de Europa con mapas y recomendaciones",
        "quantity": 85,
        "price": 19.99,
        
    },
    {
        "name": "Juego de mesa estratégico",
        "description": "Juego de mesa para toda la familia con duración de 60 minutos",
        "quantity": 40,
        "price": 39.99,
        
    },
    {
        "name": "Caja de chocolates artesanales",
        "description": "Caja con 20 chocolates artesanales variados",
        "quantity": 90,
        "price": 24.99,
        
    },
    {
        "name": "Crema hidratante natural",
        "description": "Crema hidratante con ingredientes naturales para todo tipo de piel",
        "quantity": 120,
        "price": 14.99,
        
    },
    {
        "name": "Juego de llaves de mano",
        "description": "Juego de 15 llaves de mano en acero inoxidable",
        "quantity": 55,
        "price": 29.99,
        
    },
]
