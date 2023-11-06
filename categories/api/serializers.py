from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Explanation:
    The CategorySerializer is used to serialize Category model instances into JSON data, providing a
    structured representation of the model's fields. It maps the model's fields to the serializer's
    fields specified in the 'fields' attribute.

    Usage:
    This serializer can be utilized in Django REST Framework views to convert Category model instances
    into JSON format. It automatically handles the serialization process for the specified fields.
"""
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'published']
