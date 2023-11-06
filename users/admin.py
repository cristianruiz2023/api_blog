from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin configuration for managing the built-in User model in the Django Admin panel.

    Explanation:
    The UserAdmin class provides an interface for managing the built-in User model within the Django Admin interface.
    This class extends the default UserAdmin provided by Django for customizing the display and functionalities
    related to the User model.

    Usage:
    - Inherits the BaseUserAdmin, providing extended functionalities for managing User instances.
    - This class can be further extended to add or customize functionalities related to the User model.

    Example:
    Configuring the UserAdmin for the User model in the Django Admin panel:
    ```
    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
    from django.contrib.auth.models import User

    @admin.register(User)
    class UserAdmin(BaseUserAdmin):
        pass
    ```

    Note:
    - The UserAdmin class extends the BaseUserAdmin and provides an interface for managing User instances.
    - This class can be customized to add or modify functionalities specific to managing User instances in the admin panel.
    - Ensure that the appropriate User model is imported according to your Django setup."""
    pass
