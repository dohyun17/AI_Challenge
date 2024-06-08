import requests
from bs4 import BeautifulSoup

load_url = "https://news.daum.net/politics"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

mainBox = soup.find(class_="list_newsmajor")

filename= "urls.txt"
with open(filename, "w", encoding="utf-8") as f:
    for element in mainBox.find_all("li"):
        title = element.find("a").text
        url = element.find("a").get("href")
        f.write(title + " : ")
        f.write(url)
        f.write("\n")