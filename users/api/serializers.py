from rest_framework import serializers
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """Explanation:
    The UserRegisterSerializer class handles the serialization of user data for user registration. It defines the
    necessary fields from the User model required for the registration process.

    Attributes:
    - model (User): The model associated with the serializer.
    - fields (list): Fields included in the serialization, such as 'id', 'email', 'username', and 'password'.

    Usage:
    - This serializer is used to handle user registration requests, serializing data for the creation
    of new users."""
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        """Explanation:
        The create method is used in a Django REST Framework serializer to handle the creation of a new instance.
        It takes the validated data, extracts the password field if it exists, creates a new instance of the model
        represented by the serializer, sets the password (if available), saves the instance, and returns the created instance.

        Args:
        - validated_data (dict): Validated data to create a new instance.

        Returns:
        - Instance: The newly created instance based on the validated data."""
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """Explanation:
    The UserSerializer class manages the serialization of user data for retrieval purposes. It selects specific fields
    from the User model necessary to display user information.

    Attributes:
    - model (User): The model associated with the serializer.
    - fields (list): Fields included in the serialization, such as 'id', 'email', 'username', 'first_name', and
    'last_name'.

    Usage:
    - This serializer is used to handle user data retrieval, providing specific information about a user."""
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']


class UserUpdateSerializer(serializers.ModelSerializer):
    """Explanation:
    The UserUpdateSerializer class manages the serialization of specific user data used for updating user information.
    It restricts the fields to 'first_name' and 'last_name' to enable changes to these specific user attributes.

    Attributes:
    - model (User): The model associated with the serializer.
    - fields (list): Fields included in the serialization, such as 'first_name' and 'last_name'.

    Usage:
    - This serializer is specifically designed to handle the updating of 'first_name' and 'last_name' for a user."""
    class Meta:
        model = User
        fields = ['first_name', 'last_name']