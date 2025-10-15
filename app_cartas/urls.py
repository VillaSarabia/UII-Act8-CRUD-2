# app_cartas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    # 'id' se convierte en 'pk' para ser más estándar en Django, pero mantenemos 'id' para la consistencia del ejercicio
    path('<int:id>', views.ver_carta, name='ver_carta'),
    path('agregar/', views.agregar_carta, name='agregar_carta'),
    path('editar/<int:id>/', views.editar_carta, name='editar_carta'),
    path('borrar/<int:id>/', views.borrar_carta, name='borrar_carta'),
]