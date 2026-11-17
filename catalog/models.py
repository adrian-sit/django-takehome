from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    tags = models.ManyToManyField(
    Tag,
    related_name="products",
    blank=True,
)

    def __str__(self):
        return self.name