import requests

# given a movie name
# function returns a JSON file of all matching movies from the OMDB API"""
def getMovie(movie):
    url = 'http://www.omdbapi.com/?s=%s&apikey=36921cd1' % movie
    return requests.get(url).json()