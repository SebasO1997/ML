'''1. Crear clase producto con los siguientes atributos:

- codigo
- nombre
- precio
Crearle constructor, getter y setter, y una función llamada calcular total
donde le pase unidades y calcule el precio total
'''

class Producto:

    def __init__(self, codigo, nombre, precio, descuento = None):
        self.__codigo = codigo ## __codigo: privado, ya no es accesible
        self.__nombre  = nombre
        self.__precio = precio
        self.__descuento = descuento
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    
    @property
    def precio(self):
        if self.__descuento== None:
            return self.__precio
        else: 
            return self.__descuento.aplicar_descuento(self.__precio)

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    ## Que sea pueda ver el objeto con un print
    
    def __str__(self): # cuando mostrar algo con el print
        return 'Codigo: '+ str(self.__codigo) + ' Nombre: '+ str(self.__nombre)+ ' Precio: '+ str(self.__precio)

    def calcular_total(self, unidades):
        return self.precio * unidades ## precio corresponde al getter 

'''2. Añadir clase pedido que tiene como atibutos:

- lista de productos
- lista de cantidades
Añade las siguentes funcionalidades:
- total_pedido: muestra el precio final del pedido
- mostrar_productos: muestra los productos del pedido


3. Siguiendo con la clase pedido. Añadir la siguiente funcionalidad:
- Añadir producto: le paso un producto y una cantidad, añadir el producto y cantidad a su respectiva lista
Validar que el dato que se pasa sea correcto, es decir, que sea un producto y que la cantidad sea valida.
En caso de no serlo devolver una excepcion.

- Eliminar producto: le paso el producto a borrar, si exste, se elimina. 
Comprobar tambien que es un producto lo que se pasa.
'''
class Pedido:
    
    def __init__(self):
        self.__productos = []
        self.__cantidades = []


    def añardir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto): # si producto no es instancia de la clase Producto 
            raise Exception ('añadir producto: producto debe ser de clase Producto')
        
        if not isinstance(cantidad, int): # si cantidad no es instancia de la clase int 
            raise Exception ('añadir producto: cantidad debe ser un numero entero')
        
        if cantidad <= 0:
            raise Exception('añadir producto: cantidad debe ser mayor a 0')
        
        if producto in self.__productos: # si el producto esta en el array productos, se le pone un indice
            indice = self.__productos.index(producto) # dame el indice del producto
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad

        else: ## nuevo producto
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('añadir producto: producto debe ser de clase Producto')

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        
        else: ## el producto a eliminar no existe 
            raise Exception('El producto no existe')

    def total_pedido(self):
        total = 0
        ## recorrer dos arrays a la vez
        
        for (i,j) in zip(self.__productos, self.__cantidades):
            total = total + i.calcular_total(j)
            
        return total

    def mostrar_pedido(self):
        
        for(i,j) in zip(self.__productos, self.__cantidades):
            print('( Codigo: ', str(i.codigo), ' Producto: ', i.nombre, ' Precio: ', str(i.precio), ') Cantidad: ', str(j) )

'''4. Crear clase Descuento que tiene los siguientes atributos:
- tipo: es un string y solo puede ser fijo o procentaje
- Valor: es un numero, si e fijo debe ser mayor a 0 y si es porcerntaje el valor debe estar entre 1 y 100
Tiene la siguiente funcionalidad:
- Aplicar descuanto (precio):
- Si el tipo es fijo, se le resta la cantidad al precio
- Si el tipo es porcentaje, se le resta el porcentaje al precio

añadir este descuento al producto, este será opcional y solo se aplicará si tiene descuento.
Validar que el descuento se crea correctamente
'''
TIPO_DESC_FIJO = 'Fijo'
TIPO_DESC_PORC = 'Porcentaje'

class Descuento:
    
    def __init__(self, tipo, valor):

        ## Validaciones
        if not isinstance(valor, int):
            raise ValueError('constructor descuente: valor debe ser un numero')
        if not isinstance(tipo, str):
            raise ValueError('constructor descuente: tipo debe ser un string')
        if tipo != TIPO_DESC_PORC and tipo != TIPO_DESC_FIJO:
            raise ValueError('constructor descuento:  el tipo debe ser fijo o porcentaje')
        if tipo == TIPO_DESC_FIJO and valor <= 0:
            raise ValueError('constructor descuento:  el valor en el tipo fijo debe ser mayor a 0')
        if tipo == TIPO_DESC_PORC and (valor <= 0 or valor > 100):
            raise ValueError('constructor descuento:  el valor en el tipo porcentaje debe estar entre 1 y 100')

        self.__tipo = tipo
        self.__valor = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__tipo = valor
    
    def aplicar_descuento(self, precio):

        if self.__tipo == TIPO_DESC_FIJO:
            if precio > self.__valor: # debe mayor para que no me quede negativo
                return precio - self.__valor
            else:
                return 0
        
        else: 
            return precio - (precio * (self.__valor/100))
        



## Creando objetos
        
desc1 = Descuento(TIPO_DESC_FIJO, 5)
desc2 = Descuento(TIPO_DESC_PORC, 50)

p1 = Producto(1, 'Producto 1', 5)
p2 = Producto(2, 'Producto 2', 10, desc1)
p3 = Producto(3, 'Producto 3', 15, desc2)

## Parte def __str__
print('parte __str__')
print(p1)
print(p2)
print(p3)
print('\n')

## Parte getter
# print('parte getter')
# print(p1.nombre)
# print(p2.nombre)
# print(p3.nombre)

# print('\n')
## Parte setter
# print('parte setter')
# p1.nombre ='Producto 4'
# print(p1.nombre)
# print(p2.nombre)
# print(p3.nombre)
# print('\n')

## Parte calcular unidades
# print('parte calcular unidades')
# print(p1.calcular_total(5))
# print(p2.calcular_total(5))
# print(p3.calcular_total(5))

pedido_1 = Pedido()

try:
    pedido_1.añardir_producto(p1, 5)
    pedido_1.añardir_producto(p2, 5)
    pedido_1.añardir_producto(p3, 5)
    print('Total pedido: ' + str(pedido_1.total_pedido()))
    pedido_1.mostrar_pedido()

    pedido_1.eliminar_producto(p1)

    print('Total pedido: ' + str(pedido_1.total_pedido()))

    pedido_1.mostrar_pedido()

except Exception as e:
    print(e)


