from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Custom User model inheriting from Django's AbstractUser.

    Explanation:
    The User class extends the functionality of Django's AbstractUser to include an email field as the unique
    identifier for user authentication.

    Attributes:
    - email (EmailField): A unique email address for user identification.
    - USERNAME_FIELD (str): Indicates the field used as the unique identifier for authentication (set to 'email').
    - REQUIRED_FIELDS (list): Specifies the required fields for creating a user (empty in this case).

    Usage:
    - 'email' field is used as the unique identifier for a user's email address.
    - 'USERNAME_FIELD' specifies 'email' as the field for user authentication.
    - 'REQUIRED_FIELDS' define fields required for creating a user, currently left empty.

    Example:
    Defining a custom User model in a Django application:
    ```
    class User(AbstractUser):
        email = models.EmailField(unique=True)
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
    ```

    Note:
    - The model extends AbstractUser, providing additional fields for user management.
    - Ensure to handle migrations appropriately when introducing a custom user model in a Django application.
    """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

