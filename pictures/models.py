from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length =30)


    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()

    class Meta:
        ordering = ['category_name']


class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()


class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    category = models.ForeignKey(Category, db_column='category_name')
    location = models.ManyToManyField(Location)
    image = models.ImageField(upload_to = 'imagepath/')


    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(category__category_name__contains=search_term)
        return pictures

