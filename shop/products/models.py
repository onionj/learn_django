from django.db import models

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

    def __str__(self) -> str:
        return self.title
