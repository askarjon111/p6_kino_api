from rest_framework import serializers

from apps.movies.api_endpoints.language.serializers import LanguageMiniSerializer
from apps.movies.models import MovieSubtitle


class MovieSubtitleMiniSerializer(serializers.ModelSerializer):
    language = LanguageMiniSerializer()
    
    class Meta:
        model = MovieSubtitle
        fields = ['id', 'language']

__all__ = ['MovieSubtitleMiniSerializer']
