from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """ Explanation:
    The CommentsConfig class represents the configuration for the 'comments' app. It is used to define
    settings specific to this app.

    Usage:
    - 'default_auto_field' sets the default primary key type for models in the 'comments' app to 'BigAutoField'.
    - 'name' specifies the name of the app, in this case, 'comments'."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
