from django.db import models


class Location(models.Model):
    locat = models.CharField(max_length=30)

    def __str__(self):
        return self.locat


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
    image_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls, search_term):  # search for an image using its category.
        search_result = cls.objects.filter(image_category__category__icontains=search_term)
        return search_result

    @classmethod
    def filter_location(cls, location):  # filter images by the location.
        filter_imagelocation = cls.objects.filter(image_location__locat__icontains=location)
        return filter_imagelocation

    @classmethod
    def get_image_by_id(cls, input_id):
        retrieved_image = cls.objects.get(id=input_id)
        return retrieved_image
