from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.models import Genre
from .serializers import GenreListSerializer


class GenreListView(APIView):
    def get(self, request):
        name = request.GET.get('name')
        genres = Genre.objects.all()
        if name:
            genres = genres.filter(name__icontains=name)

        serializer = GenreListSerializer(genres, many=True)

        return Response(serializer.data, status=200)


__all__ = ['GenreListView']
