from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=200)
    short_desc = models.TextField(default="")
    desc = models.TextField(default="")
    card_image = models.ImageField(upload_to='images/', default=None)
    tsne_bar_image = models.ImageField(upload_to='images/', default=None)
    tsne_full = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.name