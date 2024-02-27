## TUPLAS Y LISTAS

lista = [i for i in range(1,11,1)]
print(lista)
tupla= (1,2,3,4,5,6,7,8,9,10)
#tupla = (j for j in range(1,11,1))

# indice = int(input('Dame el indice: '))
# print(tupla[indice])

lista_2 = [k for k in range(11,21,1)]
print(lista_2)
suma_lista = []
for i_, j_ in zip(lista,lista_2):
    suma_lista.append(i_+j_)

print(suma_lista)
