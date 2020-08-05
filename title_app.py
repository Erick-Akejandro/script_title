from urllib.request import urlopen
from bs4 import BeautifulSoup

print("Por favor digite su url")
url=(str(input("Url : ")))
html =  urlopen(url)
res = BeautifulSoup(html.read(),'html5lib')
print("Aca esta la etiqueta de titulo de esta pagina ")
print(res.title)

#Tiempo maximo en respuesta 4Segundos
"""Se puede obtener cualquier etiqueta de la pagina solo cambiando 
la etiqueta que se encuentra en print(res.title) , solo tendras que cambiar el (title)
por la etiqueta que desees"""