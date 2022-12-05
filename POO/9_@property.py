# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:

# O PROPERTY se comporta
# como atributo mas é um metodo

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        print("GET COR:")
        return self.cor
    # - como getter
    # - p/ evitar quebrar código cliente
    # - p/ habilitar setter
    # - p/ executar ações ao obter um atributo
    # Código cliente - é o código que usa seu código

    @property
    def peg_cor(self):
        return self.cor

# preciso do palavra "cor"

c1 = Caneta("vermelho")
print(c1.cor) # <- palavra chave

# Palavara generica GETTER
print(c1.get_cor())

# Palavra generica como atributo por causa @property
print(c1.peg_cor)
