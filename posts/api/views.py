from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    """Explanation:
    The PostApiViewSet class serves as a viewset designed to manage API endpoints related to the Post model.
    It specifies permission classes, serializers, querysets, lookup fields, and filtering options for the view.

    Usage:
    - 'permission_classes' restrict access based on IsAdminOrReadOnly permission.
    - 'serializer_class' defines PostSerializer for JSON serialization/deserialization.
    - 'queryset' fetches all published instances of the Post model.
    - 'lookup_field' specifies the field to be used for retrieving a single instance in the view.
    - 'filter_backends' determine filtering methods such as DjangoFilterBackend.
    - 'filterset_fields' defines fields available for filtering in the view."""
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']

    # filterset_fields = ['category']
