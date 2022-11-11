import tmdb_client
from unittest.mock import Mock


def test_get_single_movie(monkeypatch):
    mock_single_movies_list = ['Movie 1']
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_single_movie("{movie_id}")
    assert movies_list == mock_single_movies_list


def test_get_single_movie_cast(monkeypatch):
    mock_single_movie_cast = ["Cast"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_single_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_cast = tmdb_client.get_single_movie("{movie_id} , {how_many}")
    assert movies_cast == mock_single_movie_cast 
    
def test_get_movie_images(monkeypatch):
    mock_movie_image = ["Image"]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_image
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_image = tmdb_client.get_movie_images("{movie_id}")
    assert movies_image == mock_movie_image