# SETTER

# O setter serve para vc poder usar o metodo como atributo
# assim como o property faz um metodo virar atributo

# lembrando que este metodo serve para deixar seguro o atributo
# __cor , ( O USO DE __ EM UMA VARIAVEL DIZ PARA NAO SER USADO ESTE ATRIBUTO)

class Caneta:
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor= cor

# sem o setter da erro atribuir
c1 = Caneta("azul")
print(c1.cor) # <- cor da caneta
# c1.cor = "verde" <- nao e possivel instanciar, pois é um metodo

# COM O SETTER
c1.cor = "verde" # <- uso do @property
print(c1.cor) # uso do setter