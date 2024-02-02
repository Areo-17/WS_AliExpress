"""from bs4 import BeautifulSoup
import requests

website = 'https://es.aliexpress.com/w/wholesale-laptop.html?spm=a2g0o.home.search.0'
result = requests.get(website)
result.status_code
200
print(result.status_code)

content = result.text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())
"""
from bs4 import BeautifulSoup
import requests

url = "https://es.aliexpress.com/w/wholesale-laptop.html?spm=a2g0o.home.search.0"
result = requests.get(url)
content = result.text 

soup = BeautifulSoup(content, 'lxml')

precios = soup.find_all('div', class_="multi--price--1okBCly")
nombres = soup.find_all('h1', class_="multi--titleText--nXeOvyr")

if not precios or not nombres:
    print("No se encontraron precios o nombre del artículo.")
else:
    for i, (precio, nombres) in enumerate(zip(precios, nombres), 1):
        print(f"Producto {i}:")
        print(f"Precio: {precio.text.strip()}")
        print(f"Nombre del artículo: {nombres.text.strip()}\n")


