# Para deixar mais facil é possivel criar um
# Valores padroes em um classe, o Init
# Metodo, que inicializa algum valor como padrao

# O metodo INIT
# Cria um molde pre definido
#
#

class Pessoa:
    def __init__(self, nome="Nao", sobrenome="Informado"):
        self.nome = nome
        self.sobrenome = sobrenome

C1 = Pessoa()
C2 = Pessoa("joao", "Cezar")

print(C1.nome, C1.sobrenome)
print(C2.nome, C2.sobrenome)