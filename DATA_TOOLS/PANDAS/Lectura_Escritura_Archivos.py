### Lectura y escritura de Archivos de Texto
import os
import pandas as pd

ruta = r'C:\Users\USUARIO\Documents\Python Scripts\ML\Scripts\POO\lectura de archivos.txt'
ruta = ruta.replace(os.sep, '/')
# archivo = open(ruta, encoding='utf-8')
# texto = archivo.read()
# linea_texto = archivo.readline()
# print(linea_texto)
# linea_texto = archivo.readline()
# print(linea_texto)
# linea_texto = archivo.readline()
# print(linea_texto)



# print(texto


# archivo.close()

## Con with no necesita el close de forma explicita 
# lectura 
# with open(ruta, 'r',encoding='utf-8') as archivo: # estructura
#     linea_texto = archivo.readlines()
#     print(linea_texto )
#     ## open funciona como para escritura o lectura. 
#     ## Para especificar en python que quiero un archivo para lectura o escritura se incluye 'r': para read, 'w': escritura
# # Escritura 
#     ## Tener en cuenta que sobreescribe la informacion que hay en el texto
# with open(ruta, 'w',encoding='utf-8') as archivo: # estructura
#     archivo.write('Minino 6 \n') # se debe agregar el salto de linea de forma explicita
#     archivo.write('ALejo 22')
    
# ## Si no quiero que se sobre escriba el archivo y en cambio lo quiero actualizar
#     ## Se cambia 'w' por 'a'
# with open(ruta, 'a',encoding='utf-8') as archivo: # estructura
#     archivo.write('\nSebas 26') # se debe agregar el salto de linea de forma explicita    

## Si el archivo no se encuentra del proyecto, como puedo cargarlo en el script?
   ## debo especificar la ruta absoluta del archivo  
    
"""
'Zocalo': [100,200,300]
'Bellas Artes': [400,500,600]
'Juarez': [700,800,900]
'Hidalgo': [1000,1100,1200]
"""

pasajeros = {} # def como nulo
ruta_datos =  r'C:\Users\USUARIO\Documents\Python Scripts\ML\Scripts\POO\datos_metro.txt'
ruta_datos =  ruta_datos.replace(os.sep, '/')
with open(ruta_datos,'r', encoding='utf-8') as file:
    file.readline() # quita encabezado, primera linea
    estaciones = file.readlines() # informacion relevante
    for estacion in estaciones:
        # Convertir el texto a diccionario 
        lista = estacion.strip().split(',')
        pasajeros[lista[0]] = list(map(int,lista[1:]))

print(pasajeros)
    