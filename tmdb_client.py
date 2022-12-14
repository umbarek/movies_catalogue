import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzODc0MTcxYWIyZjkyNTFjOTZhZmVlYWI1OTAzNDEwOSIsInN1YiI6IjYzNTk5MTg3ZTg5NGE2MDA3ZTI0MTZiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BqmwYHluaW2UFrHDlQ99mSKIm_t2V43Z87fho9roNB4"
endpoint = "https://api.themoviedb.org/3/movie/"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

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

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"][:how_many]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")

