# Dict ou Vars dicionario em atributos...

# Tanto o vars quanto o dict
# tranforma em dicionario o objeto

class Celular:

    def __init__(self, marca, modelo, cor, preco):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def patch(self):
        print(self.__dict__)

c1 = Celular("Sansung", "S20FE", "Preto", 1498.30)
c2 = Celular("Apple", "Iphone X PRO", "Preto", 3800.00)


# < --- chamada do print do objeto em dicionario
c1.patch()
