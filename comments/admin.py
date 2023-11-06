from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Explanation:
    The CommentAdmin class is a configuration for managing and displaying Comment instances within
    the Django Admin panel. It customizes the way Comment objects are presented in the admin interface.

    Usage:
    - 'list_display' specifies the fields to be shown for each Comment instance in the admin panel.
      In this case, 'content', 'user', 'post', and 'created_at' fields are displayed."""
    list_display = ['content', 'user', 'post', 'created_at']

