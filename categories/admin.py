from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """se encarga de registrar y configurar la interfaz de administración para el modelo Category.
     Aquí se define una clase CategoryAdmin que hereda de admin.ModelAdmin. Esta configuración
     personalizada se utiliza para especificar cómo se muestra y se interactúa con los objetos
     Category en el panel de administración de Django."""
    list_display = ['title', 'published']


