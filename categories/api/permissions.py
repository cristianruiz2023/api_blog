from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """The 'IsAdminOrReadOnly' permission class is designed to provide read-only access to any request
    method except for GET requests, which allows full access to authenticated users with 'is_staff'
    privilege. This means that unauthenticated or non-staff users have read-only access, while staff
    members have full access for all methods other than GET.

    Usage:
    This permission class can be applied to Django REST Framework views to control access based on
    the request method and the user's 'is_staff' status."""
    def has_permission(self, request, view):
        """Determines the permission level for a specific action based on the request method and user role.

    Parameters:
    - request: The HTTP request sent to the server.
    - view: The view associated with the request.

    Returns:
    - If the request method is 'GET', permission is granted unconditionally, allowing access.
    - For other request methods, it checks if the user making the request is a staff member.
      - Returns True if the user is a staff member, granting access.
      - Returns False if the user is not a staff member, denying access.

    Details:
    - This method is a part of a permission control system and determines whether the user has permission for a specific action based on the request method and user's staff role.
    - For 'GET' requests, permission is granted without conditions, allowing access.
    - For other request types, it checks if the user making the request is a staff member. Staff members have elevated privileges and are granted access.
    - Non-staff users are denied access for request methods other than 'GET'.
"""
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff