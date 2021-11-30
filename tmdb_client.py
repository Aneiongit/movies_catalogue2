import requests

api_token = "api_token"
endpoint = "https://api.themoviedb.org/3/movie/"
headers = {"Authorization": f"Bearer {api_token}"}


def get_popular_movies():
    response = requests.get(endpoint+f"popular", headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    response = requests.get(endpoint+f"{movie_id}", headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    response = requests.get(endpoint+f"{movie_id}/credits", headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    response = requests.get(endpoint+f"{movie_id}/images", headers=headers)
    return response.json()


def get_movies_list(list_type):
    response = requests.get(endpoint+f"{list_type}", headers=headers)
    response.raise_for_status()
    return response.json()
