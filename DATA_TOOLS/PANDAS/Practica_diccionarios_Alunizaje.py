## Practica diccionarios Alunizaje
## Conteo de palabras para analisis de sentimientos

import os

ruta = r'C:\Users\USUARIO\Documents\Python Scripts\ML\Scripts\DATA_TOOLS\PANDAS\Alunizaje.txt'
ruta = ruta.replace(os.sep, '/')

with open(ruta, 'r', encoding='utf-8') as archivo:
    texto =  archivo.read()
    #print(texto,'\n \n')

## Limpieza de simbolos que quiero quitar
    simbolos_quitar =(',','.','(',')')
    for simbolo in simbolos_quitar: # para cada simbolo en simbolos a quitar 
        texto = texto.replace(simbolo,'') # reemplazo simbolo por cadena vacia

    ## considerar las mayusculas y minisculas(para el ordenador son diferentes)
    texot = texto.upper() # todo a matusculas
    lista_texto = texto.split() # separa todas las palabras en un lista
    #print(lista_texto)
    
    ## Como contar las palabras
    ## Implementar diccionario 
    palabras = {} # diccionario nulo donde inculyen las palabras
    for palabra_texto in lista_texto:
        if palabra_texto in palabras.keys(): # si la palabra existe
            palabras[palabra_texto] = palabras[palabra_texto] + 1 # incremento el valor almacenado
        else: # si no existe
            palabras[palabra_texto] = 1
    
    ## ordenar un diccionario
    ## Convertir el diccionario a lista 
    lista_palabras =  list(palabras.items())  ## items regresa tuplas: tengo una lista de tuplas      
    ## para ordenar se utilizan funciones lambda
    ## a cada palabra dentro de listadepalabras, no las ordene por el primer elemento si no por el segundo
    # print(lista_palabras.sort(key= lambda lista_palabra: lista_palabra[1]))
    print(sorted(lista_palabras, key= lambda lista_palabra: lista_palabra[1]))
    



