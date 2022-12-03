import random

# Metodos sao funcoes em classes

class Carro:
    def __init__(self, nome="", cor="", marca=""):
        self.nome = nome
        self.cor = cor
        self.marca = marca

    # Metodo que vai aparecer alguma mensagem aleatoria ao chamar o metodo
    def aceleracao(self):
        print("%s %s %s" % (self.nome, self.cor, ["acelerou meu parceiro!", "pisou o pé no acelerador", "queimou a roda!"][ random.randint(0, 2)]))


Fusca = Carro("Fusca", "Preto", "Volskwagen")
Celta = Carro("Celta", "Branco", "Ford")

Fusca.aceleracao()
Celta.aceleracao()