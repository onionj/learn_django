from django.db import models
import os
import random
# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    _, ext = get_filename_ext(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'products/{final_name}'


class Product(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
