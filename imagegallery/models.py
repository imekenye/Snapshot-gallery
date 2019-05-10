
from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:  # Meta subclass specifies model-specific options. This helps in ordering data
        verbose_name_plural = 'Categories'

    def save_category(self):
        self.save()


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    image_path = models.ImageField(upload_to='photos/')
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()


