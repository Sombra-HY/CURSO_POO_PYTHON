# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Fabricante:
    def __init__(self, marca):
        self.marca = marca
        self._carros = []
    
    def add_car(self, *Carro):
        self._carros.extend(Carro)

    def funcionalidades(self):
        print("Marca da fabricante - %s \n"% self.marca)
        for car in self._carros:
            print("MODELO : %s\nMotor: %s\nVersao: %s\n\n"
            % (car.modelo_car, car.motor.nome_motor, car.motor.versao))


class Carro:
    def __init__(self, modelo_car):
        self.modelo_car = modelo_car
        self.motor = None

    def add_motor(self, nome_motor, versao):
        self.motor = Motor( nome_motor, versao)
    


class Motor:
    def __init__(self, nome_motor, versao):
        self.nome_motor = nome_motor
        self.versao = versao


c1 = Carro("Celta")
c1.add_motor("G1232H","2.0")

c2 = Carro("JCity")
c2.add_motor("G1232H","1.0")

f1 = Fabricante("Mercedez Bens")
f1.add_car(c1,c2)


f1.funcionalidades()










