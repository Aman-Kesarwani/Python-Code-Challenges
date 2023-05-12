import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/sql/"

response  = requests.get(url)

print(type(response))

print(response)

htmlContent = response.content

soup = BeautifulSoup(htmlContent, "html.parser")
print(soup)
print(soup.prettify)
print(type(soup))
print(soup.findAll('div'))

