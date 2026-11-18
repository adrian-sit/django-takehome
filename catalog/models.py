from django.db import models

"""
Database models for the product catalog

Defines products, categories, and tags, including their
relationships to support product searching and filtering
"""

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    related_name="products",
    )
    tags = models.ManyToManyField(
    Tag,
    related_name="products",
    blank=True,
    )

    def __str__(self):
        return self.name