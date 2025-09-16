from rest_framework import serializers
from apps.meta.models import WatchSession
from apps.movies.api_endpoints.movie.MovieDetail.serializers import MovieDetailSerializer


class WatchSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchSession
        fields = '__all__'
