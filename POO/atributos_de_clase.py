## ATRIBUTOS DE CLASE

class Vehiculo:
    numero_carro = 0
    gama_colores = ('BLANCO','NEGRO', 'ROJO', 'AZUL')

    def __init__(self, color):
        Vehiculo.numero_carro += 1
        self.serie = Vehiculo.numero_carro
        self.set_color(color)

    def __str__(self):
        return f'Serie: {self.serie}, Color: {self.color}'
    
    def set_color(self, color):
        color =  color.upper().strip()
        if color in Vehiculo.gama_colores:
            self.color = color
        else:
            self.color = Vehiculo.gama_colores[0] # default


auto_1 = Vehiculo('NEGRO')
auto_2 = Vehiculo('VERDE')

print(auto_1)
print(auto_2)

