
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_classe(self):
        print(self.nome, self.sobrenome, "na",self.__class__.__name__)



class Cliente( Pessoa):
    ... 

class Aluno( Pessoa):
    ... 

c1 = Cliente("Lucas","Sombra")
a1 = Aluno("Jose","Arruda")

c1.falar_classe()
a1.falar_classe()

# help(Cliente)
# a orden de procurar pode ser usada com o help...
# Method resolution order:
# |      Cliente
# |      Pessoa
# |      builtins.object

# CLIENTE HERDOU os metodos e atributos do Pessoa