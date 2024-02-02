from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}".capitalize()


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    img_url = models.URLField(null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name}".capitalize()


