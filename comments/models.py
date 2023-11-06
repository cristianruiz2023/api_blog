from django.db import models
from django.db.models import CASCADE
from users.models import User
from posts.models import Post


class Comment(models.Model):
    """Explanation:
    The Comment model is used to store comments made by users on specific posts. It captures the textual
    content of the comment and records the timestamp of when the comment was created. It maintains a
    relationship with both the User model (author of the comment) and the Post model (post being commented on).

    Usage:
    - 'content' stores the textual content of the comment.
    - 'created_at' is automatically populated with the date and time when the comment is created.
    - 'user' is the user who authored the comment (associated through a ForeignKey to the User model).
    - 'post' is the post on which the comment is made (associated through a ForeignKey to the Post model)."""
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)
