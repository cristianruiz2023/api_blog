from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly



class CategoryApiViewSet(ModelViewSet):
    """ Explanation:
    The CategoryApiViewSet is a viewset that handles Category model instances, enabling CRUD (Create, Read,
    Update, Delete) operations through API endpoints. It specifies various attributes to define the behavior
    and configuration of the view.

    Usage:
    - 'permission_classes' restrict access to the view using IsAdminOrReadOnly permissions.
    - 'serializer_class' specifies CategorySerializer for JSON serialization/deserialization.
    - 'queryset' filters Category instances with 'published=False' by default.
    - 'lookup_field' determines the field used for single instance lookup (in this case, 'slug').
    - 'filter_backends' specifies the filtering backend using DjangoFilterBackend.
    - 'filterset_fields' defines the fields that can be filtered in the view (e.g., 'title')."""
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    queryset = Category.objects.filter(published=False)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']