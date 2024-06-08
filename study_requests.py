import requests
url = "https://python.cyber.co.kr/pds/books/python2nd/test1.html"
response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)
print(response.status_code)
filename = "download.txt"
"""
f= open(filename, mode="w",encoding="utf-8")
f.write(response.text)
f.close()
"""
with open(filename, mode="w",encoding="utf-8")as f:
    f.write(response.text)
