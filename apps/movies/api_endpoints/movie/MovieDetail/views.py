from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.movie.MovieDetail.serializers import MovieDetailSerializer
from apps.movies.models import Movie


class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

__all__ = ['MovieDetailView']
