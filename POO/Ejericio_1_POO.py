## Ejericio 1 POO

## Tragamonedas
## Librerias 
from random import randint

class Tragamonedas:

    def __init__(self, id, premio):
        '''Constructor'''
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpoints= 0

    def __str__(self): ## Str siempre lleva un return
        
        return 'Id ' + str(self.id) +' Premio: ' + str(self.premio)
    
    def __eq__(self, otro):
        return self.monedas == otro.monedas

        
    def jugar(self):
        '''
        Funcion que ejecuta o simula cuando se hala la palanca para jugar en el tragamonedas
        
        Args:

        Returns:

        '''
        self.monedas += 1 # Cuando se juega gana una moneda el tragamonedas
        numeros_aleatorios = randint(0,9), randint(0,9), randint(0,9) # se ejecuta un numero aleatorio para los cilindros (0, 0, 0)

        if numeros_aleatorios[0] ==  numeros_aleatorios[1] == numeros_aleatorios[2]:
            self.jackpoints += 1 # Cuando se gana
            mensaje = 'Congrats! You WIN! %.02f' %self.premio
        else:
            mensaje= 'Try again'
        
        return numeros_aleatorios, mensaje
    
tragamonedas_1 = Tragamonedas(1, 1000)
tragamonedas_2 = Tragamonedas(2, 10000)

for i in range(100):
    print(tragamonedas_1.jugar())
    print(tragamonedas_2.jugar())

print(tragamonedas_1.jackpoints)
print(tragamonedas_1)

print(tragamonedas_2.jackpoints)
print(tragamonedas_2)

print(tragamonedas_1==tragamonedas_2)





