from rest_framework import serializers

from apps.movies.models import Language


class LanguageMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

__all__ = ['LanguageMiniSerializer']
