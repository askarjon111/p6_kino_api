from rest_framework import serializers

from apps.movies.models import Movie
from apps.movies.api_endpoints.subtitle import MovieSubtitleMiniSerializer


class MovieDetailSerializer(serializers.ModelSerializer):
    moviesubtitle_set = MovieSubtitleMiniSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'country', 'description',
                  'age_restriction', 'release_year', 'genres',
                  'moviesubtitle_set', 'movieaudio_set',
                  'posterimage_set', 'moviefile_set']
