from django.urls import path
from apps.movies.api_endpoints import genre
from apps.movies.api_endpoints.movie import MovieDetail

urlpatterns = [
    path('<int:pk>/', MovieDetail.MovieDetailView.as_view(), name='movie_detail'),
    path('genres/', genre.GenreListView.as_view(), name='genres_list'),
]

