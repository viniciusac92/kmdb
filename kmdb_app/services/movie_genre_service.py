import ipdb

from ..models import Genres


def movie_genre_service(serializer_data):
    genres = serializer_data.data['genres']
    genres_list = []
    for gen in genres:
        new_genre = Genres.objects.get_or_create(**gen)[0]
        genres_list.append(new_genre)

    serializer_data.data['genres'] = genres_list
    return serializer_data
