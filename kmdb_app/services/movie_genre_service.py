import ipdb

from ..models import Genres, Movies
from ..serializers import GenresSerializer, MoviesSerializer


def movie_genre_service(serializer_data):
    # ipdb.set_trace()
    # genres = serializer_data.data['genres']
    genres = serializer_data.validated_data.pop('genres')
    genres_list = []
    for gen in genres:
        # ipdb.set_trace()
        new_genre = Genres.objects.get_or_create(**gen)[0]
        # new_genre_serialized = GenresSerializer(new_genre)
        # ipdb.set_trace()
        genres_list.append(new_genre)

    # retrieve_data = serializer_data.data
    # ipdb.set_trace()
    movie_data = Movies.objects.get_or_create(**serializer_data.validated_data)[0]
    # ipdb.set_trace()
    movie_data.genres.set(genres_list)
    # ipdb.set_trace()
    # retrieve_data['genres'] = genres_list
    retrieve_movie_data = MoviesSerializer(movie_data)
    return retrieve_movie_data.data
