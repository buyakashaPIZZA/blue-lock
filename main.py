import requests
from bs4 import BeautifulSoup

bluelock_url = "https://aniwatchtv.to/watch/blue-lock-season-2-19318?ep=128447"

# get website contents and parse html
response = requests.get(bluelock_url)
html = BeautifulSoup(response.text, 'html.parser')

newText = html.find('div', {"id" : "detail-ss-list"})

# create markdown string of courses
novosti_markdown = newText.text

# write markdown file
with open("novosti.md", "w") as novosti_file:
    novosti_file.write(novosti_markdown)
