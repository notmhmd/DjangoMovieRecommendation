from django.db import models
from django.utils.text import slugify
import requests


# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    plot = models.TextField()
    director = models.CharField(max_length=255)
    cast = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    poster = models.URLField()
    backdrop_img = models.URLField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        res_info = requests.get("https://api.themoviedb.org/3/search/movie?api_key=fb88a0023aaec0e26254bc4ed6c7c2ea&query=" + self.title)
        information = res_info.json()
        try:
            self.poster = "http://image.tmdb.org/t/p/w500/" + information['results'][0]['poster_path']
            self.backdrop_img = "http://image.tmdb.org/t/p/w500/" + information['results'][0]['backdrop_path']
        except:
            self.poster = "not found"
            self.backdrop_img = "not found"
        super(Movie, self).save(*args, **kwargs)



