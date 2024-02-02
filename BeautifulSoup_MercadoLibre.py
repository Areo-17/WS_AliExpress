'''
from bs4 import BeautifulSoup
import requests

url = "https://listado.mercadolibre.com.mx/laptop#D%5BA:laptop%5D"
result = requests.get(url)
content = result.text 

soup = BeautifulSoup(content, 'lxml')

precios=soup.find('div',{'class':'ui-search-item__group ui-search-item__group--price ui-search-item__group--price-grid-container'})
nombres = soup.find('div',{'class':'ui-search-item__group ui-search-item__group--title'})

if not precios or not nombres:
    print("No se encontraron precios o nombre del artículo.")
else:
    for i, (precio, nombres) in enumerate(zip(precios, nombres), 1):
        print(f"Producto {i}:")
        print(f"Precio: {precio.text.strip()}")
        print(f"Nombre del artículo: {nombres.text.strip()}\n")
'''
from bs4 import BeautifulSoup
import requests

url = "https://www.mercadolibre.com.mx/laptop-lenovo-ideapad-156-ryzen-3-7320u-8gb-256gb-ssd/p/MLM21816271?pdp_filters=category:MLM1652#searchVariation=MLM21816271&position=1&search_layout=stack&type=product&tracking_id=4fc9cb4a-dec8-4f8d-b040-12936273c0d4"
result = requests.get(url)

if result.status_code != 200:
    print(f"Error al acceder a la página. Código de estado: {result.status_code}")
    exit()

content = result.text 
soup = BeautifulSoup(content, 'lxml')

nombres = soup.find_all('div', {'class': 'ui-pdp-header__title-container'})
precios = soup.find_all('span', {'class': 'andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact'})
caracteristicas= soup.find_all('section', {'class': 'ui-vpp-highlighted-specs pl-45 pr-45'})

if not precios or not nombres:
    print("No se encontraron precios o nombres de los artículos.")
else:
    for i, (precio, nombre,caracteristicas) in enumerate(zip(precios, nombres,caracteristicas), 1):
        print(f"Producto {i}:\n")
        print(f"Nombre del artículo: {nombre.text.strip()}")
        print(f"Precio: {precio.text.strip()}")
        print(f'Caracteristicas del producto: {caracteristicas.text.strip()}')
        
