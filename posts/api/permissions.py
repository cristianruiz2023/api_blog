from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """Explanation:
    The IsAdminOrReadOnly permission class grants read access to all users for GET requests. For other request methods,
    such as POST, PUT, DELETE, it only allows access to users identified as staff or admin.

    Methods:
    - has_permission(self, request, view): Determines if the user has permission for the specified action.
        Args:
        - request (HttpRequest): The incoming request.
        - view (View): The view the request is targeting.
        Returns:
        - bool: True if the user has permission, False otherwise.

    Usage:
    - 'has_permission' method checks the method of the request and allows read access (GET) for all users.
      It restricts other methods to users identified as staff or admin."""
    def has_permission(self, request, view):
        """Checks permission for a particular request and view combination.

    Parameters:
    - request: The HTTP request made to the server.
    - view: The view associated with the request.

    Returns:
    - If the request method is 'GET', it allows permission by returning True.
    - For any other request method, it verifies if the user making the request is a staff member.
      - Returns True if the user is a staff member, allowing access.
      - Returns False if the user is not a staff member, denying access.

    Details:
    - This function is part of a permission class and determines whether the requesting user has permission for a specific action on a view.
    - For 'GET' requests, permission is granted unconditionally, allowing access.
    - For other request types (such as 'POST', 'PUT', 'DELETE', etc.), it checks if the user making the request is a staff member.
    - Staff members have elevated privileges and are granted access; otherwise, access is denied."""
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff