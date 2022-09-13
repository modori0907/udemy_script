import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import lxml


URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text # parseするために利用するオブジェクト

soup = BeautifulSoup(website_html, "lxml")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
print(movie_titles)