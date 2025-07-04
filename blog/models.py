
# Create your models here.
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200, help_text="Qeyd: maximum 200 simvol")
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, help_text="Qeyd: şəklin ölçüsü 870 x 450 px olmalıdır")
    short_description = models.CharField(max_length=255, help_text="Qeyd: maximum 200 simvol")
    author_name = models.CharField(max_length=100, help_text="Qeyd: maximum 100 simvol")
    created_at = models.DateTimeField(auto_now_add=True)
    full_description = RichTextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
