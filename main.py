import requests
from bs4 import BeautifulSoup
import re

bl_url = "https://www.animesrbija.com/anime/blue-lock-vs-u-20-japan"

# get website contents and parse html
response = requests.get(bl_url)
html = BeautifulSoup(response.text, 'html.parser')

newText = html.find('div', {"class" : "anime-episodes"})

# create markdown string of courses
novosti_markdown = newText.text

# write markdown file
with open("novosti.md", "w") as novosti_file:
    novosti_file.write(novosti_markdown)
