from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(("https://www.billboard.com/charts/hot-100/" + date))

soup = BeautifulSoup(response.text, "html.parser")
soup_name_spans = soup.find_all("span", class_="chart-element__information__song")
song_name = [song.getText() for song in soup_name_spans]