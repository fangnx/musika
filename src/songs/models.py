from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=60)
    # optional attributes
    album = models.CharField(max_length=120, blank=True)
    genre = models.CharField(max_length=120, blank=True)
    song_file = models.FileField(default='')
    comment = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True, blank=True)

    # by_user = models.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return '/posts/' + str(self.id) + '/'
        return reverse('detail', kwargs={'id': self.id})
