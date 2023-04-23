from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, )
    price = models.IntegerField()
    address = models.CharField(max_length=200, default=None)
    num_rooms = models.IntegerField()
    square_footage = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title