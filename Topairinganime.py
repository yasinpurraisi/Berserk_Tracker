import requests
from bs4 import BeautifulSoup

def get_anime_info(anime):
    anime = anime.find('img')
    name = anime.get('alt')
    poster = anime.get('data-src')
    return name,poster


web_page = requests.get("https://aniwatchtv.to/top-airing?page=5").text
content = BeautifulSoup(web_page,'html.parser')

#title
title = content.find('title').text
print(f"Title: {title}\n\n")

# Top airing anime of today
print("*******Top airing anime of today*******\n")
top_anime = content.find_all(class_="item-top")

for i in range(3):
    name , poster  = get_anime_info(top_anime[i])
    print(f"{i+1}-{name}")
    print(f"image link : {poster}\n")




