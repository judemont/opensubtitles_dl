import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

os.makedirs("subtitles")

# opensubtitleLink = "https://www.opensubtitles.org/en/ssearch/sublanguageid-fre/idmovie-2968"
opensubtitleLink = input("opensubtitles.org link: ")
domain = urlparse(opensubtitleLink).netloc


r = requests.get(opensubtitleLink)
soup = BeautifulSoup(r.content, 'html.parser')

items = soup.find_all('tr', class_='change')

i = 0
for item in items:
    links = item.find_all("a")
    downloadLink = "https://" + domain + links[1].get("href")
    rFile = requests.get(downloadLink)

    episodeNum = item.findAll("span")[0].text

    episodeTitle = item.findAll("span")[1].text

    with open("subtitles/" + episodeNum + "_" + episodeTitle + ".zip", "wb") as f:
        f.write(rFile.content)

    i += 1
