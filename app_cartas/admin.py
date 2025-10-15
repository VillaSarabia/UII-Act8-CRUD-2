# app_cartas/admin.py
from django.contrib import admin
from .models import Carta # ¡Importa el nuevo modelo!

admin.site.register(Carta) # ¡Registra el nuevo modelo!