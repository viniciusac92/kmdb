import ipdb

from ..models import Genres, Movies
from ..serializers import GenresSerializer, MoviesSerializer


def movie_genre_post_service(serializer_data):
    genres = serializer_data.validated_data.pop('genres')
    genres_list = []
    for gen in genres:
        new_genre = Genres.objects.get_or_create(**gen)[0]
        genres_list.append(new_genre)

    movie = Movies.objects.get_or_create(**serializer_data.validated_data)[0]
    movie.genres.set(genres_list)
    retrieve_movie = MoviesSerializer(movie)
    return retrieve_movie.data
