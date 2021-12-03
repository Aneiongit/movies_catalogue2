from unittest.mock import Mock
import tmdb_client


def test_get_single_movie(monkeypatch):
    id = ['Movie 1', 'Movie 2']
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = id
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    single_movie = tmdb_client.get_single_movie(1)
    assert single_movie == id


def test_get_movie_images(monkeypatch):
    url = "https://image.tmdb.org/t/p/"
    size = "w342"
    poster = "poster"
    my_mock = Mock()
    response = my_mock.return_value
    response.return_value = url + size + poster
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    single_movie = tmdb_client.get_poster_url(poster)
    assert single_movie == url + size + "/" + poster


def test_get_movie_cast(monkeypatch):
    id = {"cast": "movie1"}
    my_mock = Mock()
    response = my_mock.return_value
    response.json.return_value = id
    monkeypatch.setattr("tmdb_client.requests.get", my_mock)
    single_movie = tmdb_client.get_single_movie_cast(1)
    assert single_movie == "movie1"