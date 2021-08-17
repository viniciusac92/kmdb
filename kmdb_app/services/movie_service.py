from ..models import Genres


def movie_genre(**validated_data):
    genres = validated_data['genres']
    genres_list = []
    for gen in genres:
        new_genre = Genres.objects.get_or_create(**gen)[0]
        genres_list.append(new_genre)

    validated_data['genres'] = genres_list
    return validated_data
