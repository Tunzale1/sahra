
# Create your models here.
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icon_class = models.CharField(max_length=100, help_text="Example: tji-service-1")
    image = models.ImageField(upload_to='service_images/', blank=True)
    short_description = models.CharField(max_length=255)
    full_description = RichTextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
