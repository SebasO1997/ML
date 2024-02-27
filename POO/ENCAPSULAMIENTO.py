## ENCAPSULAMIENTO

class Cuenta:

    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__balance = 0.00

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, nuevo_direccion):
        self.__direccion = nuevo_direccion
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, nuevo_balance):
        self.__balance = nuevo_balance

    def retirar(self, retiro):
        if retiro < self.__balance:
            self.__balance = self.__balance - retiro
        else: 
            print('No posee fondos suficientes ')

    def depositar(self, deposito):
        if deposito > 0:
            self.__balance = self.__balance + deposito
        else: 
            print('El deposito debe ser mayor a 0')
    def __str__(self):
        return f'Nombre: {self.__nombre}, Balance: {self.__balance}'
    
    def mostrar_cliente(self):
        return f'Cliente: {self.__nombre}, Balance: {self.__balance}'

    
cliente_1 = Cuenta('Sebas', 'Calatrava')
print(cliente_1.mostrar_cliente())

cliente_1.nombre = 'Sebastian'
# cliente_1.balance = 1000

cliente_1.depositar(1000)
print(cliente_1.mostrar_cliente())

cliente_1.retirar(1500)
print(cliente_1.mostrar_cliente())


