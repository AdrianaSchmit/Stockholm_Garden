from django.db import models

from products.models import Product


class Reviews(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=False)

    def __str__(self):
        return self.text