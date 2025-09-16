from django.db import models
from apps.common.models import BaseModel
from apps.movies.models import Country, Language, Movie, MovieSubtitle, MovieFile


class WatchSession(BaseModel):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    device = models.CharField(max_length=200, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    country = models.ForeignKey(Country,on_delete=models.PROTECT, blank=True, null=True)
    subtitle = models.ForeignKey(MovieSubtitle, on_delete=models.PROTECT, blank=True, null=True)
    quality = models.CharField(max_length=10, choices=MovieFile.QUALITY_CHOICES, default='720p')

    def __str__(self):
        return f"WatchSession: {self.movie.title} ({self.language})"
