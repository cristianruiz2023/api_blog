from django.db import models


class Category(models.Model):
    """Attributes:
    - title (CharField): The title/name of the category, limited to a maximum of 255 characters.
    - slug (SlugField): A unique identifier used in URLs for the category, limited to 255 characters.
    - published (BooleanField): Indicates if the category is published or not. Default is set to False.

    Usage:
    The Category model is used to categorize different types of content, providing a way to organize
    and filter information. The 'title' field defines the name of the category, 'slug' is used for
    creating SEO-friendly URLs and 'published' determines its visibility."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title