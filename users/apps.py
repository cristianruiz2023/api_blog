from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Explanation:
    The UsersConfig class represents the configuration for the 'users' app within a Django project. It holds specific
    settings and behaviors for this particular app.

    Attributes:
    - default_auto_field (str): Specifies the default primary key type for models in the app.
    - name (str): Name of the app, 'users'.

    Usage:
    - 'default_auto_field' sets the default primary key type for models in the 'users' app to 'BigAutoField'.
    - 'name' specifies the name of the app, in this case, 'users'."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
