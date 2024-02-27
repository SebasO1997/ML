import numpy as np


## Crear arrays

# arreglo_1 = np.array([1,2,3,4,5,6])
# arreglo_2 = np.arange(1,7)
# print(arreglo_1)
# print(arreglo_2)


# arreglo_3 = np.array([1,2,3,4,5,6], dtype='i')
# print(f'arreglo_3: {arreglo_3}, arreglo_3.dtype: {arreglo_3.dtype}, arreglo_3.itemsize: {arreglo_3.itemsize}')

# ## Si quiero utilizar un numero diferentes de bytes
# arreglo_3 = np.array([1,2,3,4,5,6], dtype='i2') # i2: dos bytes
# print(f'arreglo_3: {arreglo_3}, arreglo_3.dtype: {arreglo_3.dtype}, arreglo_3.itemsize: {arreglo_3.itemsize}')


# arreglo_3 = np.array([1,2,3,4,5,6], dtype='i8') # i2: dos bytes
# print(f'arreglo_3: {arreglo_3}, arreglo_3.dtype: {arreglo_3.dtype}, arreglo_3.itemsize: {arreglo_3.itemsize}')


# ## Tamaño de los arreglos
# arreglo_1.shape # shape: es multidimensional tiene formato tupla
# print(f'Shape: {arreglo_1}')

# ## Modificar el tamaño
# print(f'Reshape 1:\n{arreglo_1.reshape((2,3))}') # se pasa una nueva tupla que modifica el tamaño del arreglo

# print(f'Reshape 2:\n{arreglo_1.reshape((3,2))}') 


# ## Agregar Elementos

# print(f'Agregar: {np.append(arreglo_1, 7)}')

# ## Insertar elemento
# print(f'Insertar: {np.insert(arreglo_1, 1, 7)}') # insert(arreglo, posicion, valor)

# ## Borrar elemento
# print(f'Borrar: {np.delete(arreglo_1,2)}') # delete(arreglo, posicion)


# ## Busqueda de un elemento
# print(np.where(arreglo_1 == 6)) # Retonar la posicion y el tipo de dato

# ### Practica con ejemplo

# ## operaciones vectoriales

# ## Operaciones
# print(f'Suma: {arreglo_1+1}')
# print(f'Resta: {arreglo_1-1}')
# print(f'Multiplicacion: {arreglo_1*2}')

# ## Matricial
# print(f'Matricial: {arreglo_1*arreglo_1}')



# ## Busquedas y Filtrado de Datos

# ## Busquedas 
# arreglo_busqueda =  np.array([11,12,13,14,15,16,17])

# ## Buscar elementos y retorna indice
# print(np.where(arreglo_busqueda == 11))
# print(np.where(arreglo_busqueda > 11))
# print(np.where(arreglo_busqueda < 14))

# ## Aplicar filtro a traves de vectores booleanos

# filtro = [True, False, False, True, True, False, True] 

# print(f'Filtro: {arreglo_busqueda[filtro]}') # cuando le paso un vector debe tener una relacion 1 a 1


# ## Ejemplo:

# paises = np.array(['Argentina','Bolivia','Colombia','Ecuador','Chile', 'Peru', 'Venenzuela', 'Uruguay','Brasil'])
# peso = np.random.randint(80,95, size=(9))
# altura = np.random.uniform(1.6,1.9, size=(9))

# print(f'Filtro de paises con peso mayor a 85: \n{paises[peso>85]}, \nNumero de paises: {paises[peso>85].size}')
# print(f'Filtro de paises con altura mayor a 1.75: \n{paises[altura>1.75]}, \nNumero de paises: {paises[altura>1.75].size}')


# ## Doble filtro
# print(f'Paises con peso menor a 90 y altura mayor 1.80: {paises[(peso<90) & (altura> 1.80)]}, \nNumero paises: {paises[(peso<90) & (altura> 1.80)].size}')
# print(f'Paises con peso menor a 90 o altura mayor 1.80: {paises[(peso<90) | (altura> 1.80)]}, \nNumero paises: {paises[(peso<90) | (altura> 1.80)].size}')


# ## Agregacion y Ejes de arrays para procesar Datos

# altura = np.random.uniform(1.70, 1.90, size=(5))
# pesos = np.random.uniform(70, 90, size=(5))
# print(altura)
# print(pesos)

# altura_pesos = np.concatenate((altura.reshape(5,1), pesos.reshape(5,1)),axis=1)
# # print(altura_pesos)

# print(f'Minimo: {altura_pesos.min()}')
# print(f'Maximo: {altura_pesos.max()}')
# print(f'Posicion Minimo: {altura_pesos.argmin()}') # donde esta el minimo 
# print(f'Posicion Maximo: {altura_pesos.argmax()}') # donde esta el maximo

# ## Sumas de los valores
# print(f'Suma: {altura_pesos.sum()}')
# print(f'Media: {altura_pesos.mean()}')

# ## Dimension 
# print(f'Dimension: {altura_pesos.ndim}')
# ## Forma
# print(f'Forma: {altura_pesos.shape}')

# ## Sumas por columna
# ## axis = 0
# print(f'Minimo: {altura_pesos.min(axis=0)}')
# print(f'Maximo: {altura_pesos.max(axis=0)}')
# print(f'Posicion Minimo: {altura_pesos.argmin(axis=0)}') # donde esta el minimo 
# print(f'Posicion Maximo: {altura_pesos.argmax(axis=0)}') # donde esta el maximo
# print(f'Suma alturas: {altura_pesos.sum(axis=0)}') # axis=0 Columna


# ## Union y separacion de Arrays
# altura = np.random.uniform(1.70, 1.90, size=(5))
# pesos = np.random.uniform(70, 90, size=(5))

# ## Elementos de Union

# ## STACK
# print(f'Stakc Axis = 0 {np.stack((altura, pesos), axis=0)}') # recibe tupla de los arrays a unir
# print(f'Stack Axis = 1 {np.stack((altura, pesos), axis=1)}') # recibe tupla de los arrays a unir

# ## CONCATENATE
# print(f'Concatenate  {np.concatenate((altura, pesos))}') # recibe tupla de los arrays a unir

# ## Separa datos

# ## Split
# union = np.stack((altura, pesos), axis=1)
# print(f'Union: {union, type(union)}')

# separados = np.split(union,5) # 2 secciones
# print(f'Separados: {separados, type(separados)}')


## ACELERAR EL PROCESAMIENTO DE DATOS CON FUCIONES UNIVERSALES (UFUNCS)

array_1 = np.array([1,2,3,4,5,6])
array_2 = np.array([11,12,13,14,15,16])

## Operaciones vectoriales sobre los arreglos
print('Suma add', np.add(array_1,array_2)) # es una funcion vectorial y se ejecuta en c o c++ por lo que es más eficiente
print('Resta subtract', np.subtract(array_1,array_2)) # es una funcion vectorial y se ejecuta en c o c++ por lo que es más eficiente
print('Divide', np.divide(array_1,array_2)) # es una funcion vectorial y se ejecuta en c o c++ por lo que es más eficiente
print('Multiply', np.multiply(array_1,array_2)) # es una funcion vectorial y se ejecuta en c o c++ por lo que es más eficiente
print('Potencia', np.power(array_1, 2)) # es una funcion vectorial y se ejecuta en c o c++ por lo que es más eficiente
print('Absoluto', np.absolute(array_1)) # es una funcion vectorial y se ejecuta en c o c++ por lo que es más eficiente

# Descata la eficiencia en las operaciones

altura = np.random.uniform(1.70, 1.90, size=(5))
pesos = np.random.uniform(70, 90, size=(5))
# No es funcion uiversal y no se ejecuta como vectorialmente

def calcular_imc(pesos, altura):
    return pesos/altura*altura



## Para convertir cualquier funcion a fucion vectorial se usa 
from time import perf_counter # informa el numero de segundos que pasaron
inicio = perf_counter() # punto de inicio

calcular_imc_ufunc = np.frompyfunc(calcular_imc, 2,1) #(funcion, parametros entrada, parametros salida )
print(f'Tipo: {type(calcular_imc_ufunc)}')
print(f'Imc: {calcular_imc(pesos, altura)}')
print(f'Imc: {calcular_imc_ufunc(pesos, altura)}')


for i in range(10000):
    calcular_imc(pesos, altura)

final = perf_counter()

print(f'Tiempo de ejecucion: {final-inicio}')

