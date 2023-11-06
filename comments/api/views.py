from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework  import DjangoFilterBackend

from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    """Explanation:
    The CommentApiViewSet is a viewset designed to handle Comment model instances, enabling CRUD (Create, Read,
    Update, Delete) operations through API endpoints. It defines various attributes to configure the behavior
    and filtering options for the view.

    Usage:
    - 'permission_classes' restrict access to the view using IsOwnerOrReadAndCreateOnly permissions.
    - 'serializer_class' specifies CommentSerializer for JSON serialization/deserialization.
    - 'queryset' fetches all instances of Comment model for the view.
    - 'filter_backends' specifies filtering backends including OrderingFilter and DjangoFilterBackend.
    - 'ordering' sets the default order of Comment instances by their creation date in descending order.
    - 'filterset_fields' defines the fields available for filtering in the view (e.g., 'post')."""
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    # se antepone el "-" para que ordene de forma descendente
    filterset_fields = ['post']
