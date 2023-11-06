from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Explanation:
    The PostAdmin class is an administrative configuration used to customize and manage Post instances within
    the Django Admin interface. It specifies the fields to be shown in the admin panel for Post objects.

    Usage:
    - 'list_display' determines which fields will be visible for each Post instance in the admin panel.
      In this case, 'title', 'user', 'category', 'created_at', and 'published' fields are displayed."""
    list_display = ['title', 'user', 'category', 'created_at', 'published']

