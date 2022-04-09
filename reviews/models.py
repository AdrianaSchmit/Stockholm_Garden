from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from products.models import Product


# Product Review
RATING=(
    (1,'1 star'),
    (2,'2 stars'),
    (3,'3 stars'),
    (4,'4 stars'),
    (5,'5 stars'),
)

class Reviews(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.DecimalField(choices=RATING, max_digits=2, decimal_places=0, null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text