from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    """Explanation:
    The PostSerializer class is responsible for converting instances of the Post model into JSON format for API
    representation. It includes nested User and Category serializers for related fields to provide a comprehensive
    JSON representation of Post instances.

    Attributes:
    - model (Post): The model associated with the serializer.
    - fields (list): Fields of the Post model included in the serialization.
    - user (UserSerializer): Serializer for the User model related to the Post model.
    - category (CategorySerializer): Serializer for the Category model related to the Post model.

    Usage:
    - 'model' attribute refers to the Post model, indicating the model to be serialized.
    - 'fields' attribute specifies the fields from the Post model to include in the JSON output.
    - 'user' and 'category' are nested serializers for related User and Category instances."""
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'slug',
                  'miniature',
                  'created_at',
                  'published',
                  'user',
                  'category'
                  ]
