## Diccionarios

'''
Persona
Llave: nombre, edad, direccion, altura, peso

valores: Sebas, 23, Calatrava, 1.70, 80

'''
## Creacion simple de un diccionario
persona = {'nombre': 'Sebas', 'edad': 26, 'direccion': 'Calatrava' }
print(persona)
## Acceso al valor asociado a una llave
print(persona['nombre'])
print(persona.get('nombre'))


for valor in persona.values():
    print(f'valor: {valor}')

for llave  in persona.keys():
    print(f'llave: {llave}')

for elemento in persona.items():
    print(f'elemento: {elemento}')

# print(persona.keys())
# print(persona.items())
# print(persona.items())
    
for llave, valor in persona.items():
    print(f'llave: {llave}, valor: {valor}')


## para modificar valores o agregar una nueva llave(altura)
persona.update({'direccion': 'Guaranday', 'altura':1.72}) # recibe un diccionario 

print(persona.items())

## Como agregar un solo valor asociado a una llave
persona['peso'] = 80
print(persona.items())

## Como borrar valores
## Metodo pop
persona.pop('peso') # paso la llave que quiero eliminar
print(persona.items())







