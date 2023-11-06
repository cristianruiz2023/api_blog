from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category


class Post(models.Model):
    """Explanation:
    The Post model is designed to store information about blog posts. It includes fields such as title,
    content, slug, image, creation timestamp, publication status, and relationships with User and Category.

    Usage:
    - 'title' stores the title of the post.
    - 'content' contains the textual content of the post.
    - 'slug' is a unique identifier typically used for SEO-friendly URLs.
    - 'miniature' holds an image associated with the post.
    - 'created_at' is automatically set to the date and time of post creation.
    - 'published' defines whether the post is published or not.
    - 'user' is the author of the post (linked through a ForeignKey to the User model).
    - 'category' represents the category to which the post is associated (linked through a ForeignKey to
    the Category model)."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title