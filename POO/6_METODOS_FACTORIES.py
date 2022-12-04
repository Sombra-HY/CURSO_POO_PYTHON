# Metodo de Classe

# Um metodo da classe cria um objeto e
# o cls == Pessoa é classe ao chama/ retorna a chamada da funcao vc
# acaba instanciando os valores

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # Metodo
    def mostrar(self):
        print(self.nome, self.sobrenome)

    # Aqui ha uma criacao de um objeto
    @classmethod
    def mostraar(cls, nome):
        return cls(nome, "arruda")



n1 = Pessoa("lucas", "jose") # Istanciei
n2 = Pessoa.mostraar("luis") # Metodo da claase que cria um objeto
n1.mostrar()
n2.mostrar()