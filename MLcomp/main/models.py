from django.db import models
from cloudinary.models import CloudinaryField

class Dataset(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default="")
    short_desc = models.TextField(default="")
    desc = models.TextField(default="")
    card_image = CloudinaryField('image', folder="MLcomp")
    tsne_bar_image = CloudinaryField('image', folder="MLcomp")
    tsne_full = CloudinaryField('image', folder="MLcomp")

    def __str__(self):
        return self.name