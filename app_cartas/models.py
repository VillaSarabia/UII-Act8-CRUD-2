# app_cartas/models.py
from django.db import models

class Carta(models.Model):
    nombre_carta = models.CharField(max_length=100)
    rareza = models.CharField(max_length=50)  # Común, Rara, Holo, etc.
    condicion = models.CharField(max_length=50) # Near Mint, Excellent, Poor, etc.
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2) # Para precios
    id_expansion = models.CharField(max_length=20) # Por ejemplo: "Base Set", "Fusión Strike", etc.

    def __str__(self):
        # Muestra el nombre y la rareza para identificarla fácilmente en el admin.
        return f'{self.nombre_carta} ({self.rareza}) - {self.condicion}'