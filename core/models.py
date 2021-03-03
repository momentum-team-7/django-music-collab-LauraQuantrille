from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.CharField(max_length=280)
    release_date = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Artist(models.Model):
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="artists")

    def __str__(self):
        return self.artist







#     # connect it to Album, use example from django docs and try to have a separate page to render the artists- needs to have foreign key, for each artist you want album to render
#     # new view, new template, new model, relate 2 models together, new url