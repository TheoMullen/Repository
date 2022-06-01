import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
text = response.text
soup = BeautifulSoup(text, "html.parser")

info = soup.select(selector=".article-title-description__text h3")

ranked_list = [item.getText() for item in info]
ranked_list.reverse()

with open("movies.txt", mode="w") as page:
    for item in ranked_list:
        page.write(item + "\n")
