import requests
from bs4 import BeautifulSoup

load_url = "https://python.cyber.co.kr/pds/books/python2nd/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

chap2 = soup.find(id="chap2")
for element in chap2.find_all("li"):
    print(element.text)