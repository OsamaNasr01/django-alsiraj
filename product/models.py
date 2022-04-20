from django.db import models
from sqlalchemy import true

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now=true)
    slug = models.SlugField(auto_created=true, unique=true)