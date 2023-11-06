from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Explanation:
    The CommentSerializer class is designed to transform instances of the Comment model into JSON
    format for API representation. It specifies the model to be serialized and the fields to include.

    Attributes:
    - model (Comment): The model associated with the serializer.
    - fields (list): Fields of the Comment model included in the serialization.

    Usage:
    - 'model' attribute refers to the Comment model, indicating the model to be serialized.
    - 'fields' attribute specifies the fields from the Comment model to include in the JSON output.
"""
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post'
                  ]