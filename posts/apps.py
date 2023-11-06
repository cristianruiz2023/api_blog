from django.apps import AppConfig


class PostsConfig(AppConfig):
    """ Explanation:
    The PostsConfig class represents the configuration for the 'posts' app within a Django project. It defines
    specific settings and behavior for this particular app.

    Usage:
    - 'default_auto_field' sets the default primary key type for models in the 'posts' app to 'BigAutoField'.
    - 'name' specifies the name of the app, in this case, 'posts'."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
