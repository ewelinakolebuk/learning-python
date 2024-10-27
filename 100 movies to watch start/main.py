import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_online_content = response.text
soup = BeautifulSoup(empire_online_content, "html.parser")

# title = (soup.select_one("h3")).getText()
# print(title)
titles = soup.find_all("h3")
titles_list = [title.getText() for title in titles]
print(titles_list)
titles_list = titles_list[::-1]
print(titles_list)
with open ("movies.txt", "w",encoding="utf-8") as file:
    for title in titles_list:
        file.write(f"{title}\n")





