import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_text = response.text

soup = BeautifulSoup(web_text, "html.parser")
all_title = soup.find_all(name="h3", class_="title")
title_list = [title.getText() for title in all_title][::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in title_list:
        file.write(title + "\n")

