### Intro Visualizacion de datos

import matplotlib.pyplot as plt
import numpy as np

años = []
años_ = np.arange(2011,2021,1)
for i in años_:
    años.append(str(i))
    
# print(años)

# datos_1 = np.arange(10,60,5)
# datos_2 = np.arange(20,70,5)


# plt.plot(años, datos_1)
# plt.plot(años, datos_2)
# plt.show()

# puntajes_nivel_1 =  np.random.uniform(0, 50, size=(10))
# puntajes_nivel_2 =  np.random.uniform(20, 70, size=(10))
# puntajes_nivel_3 =  np.random.uniform(30, 80, size=(10))
# puntajes_nivel_4 =  np.random.uniform(40, 90, size=(10))
# puntajes_nivel_5 =  np.random.uniform(60, 100, size=(10))


# ## Presentacion de las graficas 

# plt.plot(años, puntajes_nivel_1, label ='Nivel 1', color= 'b', marker='o', linestyle='-')
# plt.plot(años, puntajes_nivel_2,label ='Nivel 2', color= 'r',marker='<', linestyle='--')
# plt.plot(años, puntajes_nivel_3, label ='Nivel 3', color = 'g', marker='*', linestyle=':')
# plt.plot(años, puntajes_nivel_4, label ='Nivel 4', color='k', marker='^', linestyle='-.')

# ## Activar leyendas
# plt.legend()

# ## Titulo 
# plt.title('Examen Cerificacion estudiantes')

# ## Etiquetas de los ejes 
# plt.xlabel('Años que se ha realizado el examen')
# plt.ylabel('Puntaje')

# ## Personalizar eje de puntaje  0 a 1000 en incremento de 50  
# plt.yticks(np.arange(0,101,5))

# ## Cuadricula (Grilla)
# plt.grid()

# ## Activar marcas menores (ticks)
# plt.minorticks_on()

# plt.show()


## Grafica de barras vertical 

# array_barras = np.arange(0,10)

## Para evitar el solapamiento de los datos en las barras  se agrega desfase sumando al eje 
# plt.bar(array_barras+.2, puntajes_nivel_1, width=1/5)# width : acnoho de las barras
# plt.bar(array_barras+.3, puntajes_nivel_2, width=1/5)# width : acnoho de las barras
# plt.bar(array_barras+.4, puntajes_nivel_3, width=1/5)# width : acnoho de las barras
# plt.bar(array_barras+.5, puntajes_nivel_4, width=1/5)# width : acnoho de las barras
# plt.bar(array_barras+.6, puntajes_nivel_5, width=1/5)# width : acnoho de las barras
# plt.show()


## Grafica de barras horizontal
# plt.barh(array_barras+.2, puntajes_nivel_1, height=1/5)# width : acnoho de las barras
# plt.barh(array_barras+.3, puntajes_nivel_2, height=1/5)# width : acnoho de las barras
# plt.barh(array_barras+.4, puntajes_nivel_3, height=1/5)# width : acnoho de las barras
# plt.barh(array_barras+.5, puntajes_nivel_4, height=1/5)# width : acnoho de las barras
# plt.barh(array_barras+.6, puntajes_nivel_5, height=1/5)# width : acnoho de las barras
# plt.show()


## Graficas barras verticales apiladas
# plt.bar(array_barras, puntajes_nivel_5, label = 'Nivel 5')# width : acnoho de las barras
# plt.bar(array_barras, puntajes_nivel_4, bottom=puntajes_nivel_5, label = 'Nivel 4')# width : acnoho de las barras
# plt.bar(array_barras, puntajes_nivel_3, bottom=puntajes_nivel_4+puntajes_nivel_5, label = 'Nivel 3')# width : acnoho de las barras
# plt.bar(array_barras, puntajes_nivel_2, bottom=puntajes_nivel_3+puntajes_nivel_4+puntajes_nivel_5,label = 'Nivel 2')# width : acnoho de las barras
# plt.bar(array_barras, puntajes_nivel_1, bottom=puntajes_nivel_2+puntajes_nivel_3+puntajes_nivel_4+puntajes_nivel_5, label = 'Nivel 1')# width : acnoho de las barras
# plt.legend()
# plt.show()


# ## Grafica de dispersion

# plt.scatter(array_barras, puntajes_nivel_1, marker='*')
# plt.scatter(array_barras, puntajes_nivel_2, marker='*')
# plt.scatter(array_barras, puntajes_nivel_3, marker='*')
# plt.scatter(array_barras, puntajes_nivel_4, marker='*')
# plt.scatter(array_barras, puntajes_nivel_5, marker='*')
# plt.show()


## Grafico de pie

# plt.pie(puntajes_nivel_1, labels=['Argentina','Bolivia','Colombia','Ecuador','Chile', 'Peru', 'Venenzuela', 'Uruguay','Brasil','Panama'])
# plt.show()


## Combinar graficas 

# plt.bar(array_barras, puntajes_nivel_1, width=1/5)
# plt.bar(array_barras, puntajes_nivel_2, width=1/5)

# plt.plot(años, puntajes_nivel_3)
# plt.scatter(array_barras, puntajes_nivel_4)
# plt.scatter(array_barras, puntajes_nivel_5)

# plt.show()


## VISUALIZACION ESTADISTICA CON SEABORN 
    
