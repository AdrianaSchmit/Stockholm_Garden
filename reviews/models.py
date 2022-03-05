from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    rating = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=False,
        validators=[MaxValueValidator(5), 
        MinValueValidator(1)])
    #rating = models.BooleanField(default=True, null=True, blank=True)
    #rating=models.CharField(choices=RATING,max_length=150)

    def __str__(self):
        return self.text