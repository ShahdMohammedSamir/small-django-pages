from django.db import models # type: ignore

class Plant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="plants/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

