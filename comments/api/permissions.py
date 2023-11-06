from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    """Explanation:
    The IsOwnerOrReadAndCreateOnly permission class governs access to Comment instances within views. It grants
    permissions for read (GET) and create (POST) requests to all users. However, for other request methods such as
    PUT, PATCH, DELETE, it allows access only to the owner of the specific Comment instance.

    Methods:
    - has_permission(self, request, view): Determines if the user has permission for the specified action.
        Args:
        - request (HttpRequest): The incoming request.
        - view (View): The view the request is targeting.
        Returns:
        - bool: True if the user has permission, False otherwise.

    Usage:
    - 'has_permission' method checks the method of the request and permits GET and POST requests for all users.
    - For other methods, it ensures that the requesting user is the owner of the specific Comment instance.
"""
    def has_permission(self, request, view):
        """Determines if a user has permission to perform a specific action on a comment.

    Parameters:
    - request: The HTTP request made to the server.
    - view: The view associated with the request.

    Returns:
    - If the request method is 'GET' or 'POST', permission is granted unconditionally, allowing access.
    - For other request methods, it checks if the user making the request is the owner of the comment being accessed.
      - Returns True if the user is the owner of the comment, allowing access.
      - Returns False if the user is not the owner of the comment, denying access.

    Details:
    - This method is part of a permission-handling system and determines whether the user has permission to perform a
    specific action on a comment.
    - For 'GET' or 'POST' requests, permission is granted without conditions, allowing access.
    - For other request methods, it checks if the user making the request is the owner of the comment being accessed.
    - Access is granted if the user is the owner of the comment; otherwise, access is denied."""
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)

            id_user = request.user.pk
            id_user_comment = comment.user_id

            if id_user == id_user_comment:
                return True

            return False
