import requests

img_url = "http://letscoding.kr/img/image01.jpeg"
response = requests.get(img_url)

filename = img_url.split("/")[-1]
with open(filename, mode="wb") as img :
    img.write(response.content)