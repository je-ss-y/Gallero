from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length =30)


    def __str__(self):
        return self.category_name

        class Meta:
        ordering = ['category_name']


class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

