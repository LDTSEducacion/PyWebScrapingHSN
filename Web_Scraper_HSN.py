import requests
import csv
import time
from bs4 import BeautifulSoup

# URLs en la que haremos scraping
URLs = [
    "https://www.hsnstore.com/nutricion-deportiva/proteinas",
    "https://www.hsnstore.com/nutricion-deportiva/creatina",
    "https://www.hsnstore.com/nutricion-deportiva/anabolicos-naturales",
    "https://www.hsnstore.com/nutricion-deportiva/barritas",
    "https://www.hsnstore.com/nutricion-deportiva/ganadores-de-peso"
    ]

# Lista donde guardaremos los datos
datos = [
    ["Brand", "Title", "Rating", "Description"]
]

# Tiempo de inicio
tiempo_inicio = time.time()

for url in URLs:
    page = requests.get(url)

    # Parseamos el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtenemos todos los suplementos de la pagina
    elements = soup.find_all("div", class_="product_list_detailed_box")

    # Recorremos los suplementos para ir uno por uno
    for element in elements:
        # Marca del suplemento
        brand = element.find("div", class_="brand_link").text.strip()
        # Titulo del suplemento / Nombre
        title = element.find("div", class_="product_name_link").text.strip()
        # Valoracion del suplemento
        rating = element.find("span", class_="amount").text.strip()
        # Numero de valoraciones
        numberRating = ''.join(filter(str.isdigit, rating))
        # Descripcion del suplemento
        description = element.find("p", class_="product_desc_text").text.strip()

        # Agregamos los datos a la lista datos
        datos.append([brand, title, numberRating, description])


# Creamos el fichero archivoHSN.csv y escribimos los datos en el
with open('archivoHSN.csv', 'w', encoding='utf-8', newline='') as fichero:
    escritor_csv = csv.writer(fichero, delimiter=';')
    escritor_csv.writerows(datos)
    print('Se ha creado el fichero csv correctamente')

# Tiempo de fin
tiempo_fin = time.time()

# Calcula tiempo
tiempo_total = tiempo_fin - tiempo_inicio

# Mostramos por consola el tiempo total
print(f"El código ha tardado {tiempo_total}s")