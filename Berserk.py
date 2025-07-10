import requests
from bs4 import BeautifulSoup
from os import system

def get_chapter_info(chapter):
    chapter = chapter.find('a')
    text = chapter.get_text(strip=True)
    link = chapter.get('href')
    return text,link

def Load_webpage():
    web_page = requests.get("https://theberserkmanga.com")
    if web_page.status_code == 200:
        print("connected to website.\n")
    else:
        print("failed to connect.")
    data = web_page.text
    content = BeautifulSoup(data,'html.parser')

    # Title of web site :
    title = content.select("title")
    title = title[0]
    print(f"{title.text[:13]}")

    # all chapters in home page
    chapters =  content.find_all(class_="entry-title")

    # newest chapter
    text,link = get_chapter_info(chapters[0])
    print(f"""
    ***Latest Chapter***
    ****{text[8:19]}*****
    {link}
    """)

    # rest of chapters
    for i in range(1,10):
        text,link = get_chapter_info(chapters[i])
        print(f"{text} : {link}")

# main loop
Load_webpage()
while True:
    user_input = input("""
    1-Refresh
    2-exit
    your input : """)
    if user_input == "1":
        system('cls')
        Load_webpage()
    elif user_input == "2":
        print("Bye Bye")
        break
    else:
        print("invalid input")




