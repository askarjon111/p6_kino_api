from django.db import models
from apps.common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Language(BaseModel):
    name = models.CharField(max_length=100, unique=True)


class Country(BaseModel):
    name = models.CharField(max_length=200)

class Movie(BaseModel):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    age_restriction = models.PositiveSmallIntegerField(default=0)
    release_year = models.DateField()
    genres = models.ManyToManyField("Genre", related_name="movies")

    def __str__(self):
        return self.title


class MovieAudio(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.movie.title} ({self.language} audio)"


class MovieSubtitle(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.movie.title} ({self.language} subtitle)"


class PosterImage(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="movies/posters/")

    def __str__(self):
        return f"Poster for {self.movie.title} ({self.language})"


class MovieFile(BaseModel):
    QUALITY_CHOICES = [
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
        ('4K', '4K'),
    ]
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    file = models.FileField(upload_to="movies/videos")
    quality = models.CharField(choices=QUALITY_CHOICES, default=QUALITY_CHOICES[2][0])

    def __str__(self):
        return f"File: {self.movie.title} ({self.language})"
