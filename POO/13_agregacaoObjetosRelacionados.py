# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação

class Carrinho:
    def __init__(self):
        self.__produtos = []

    def append_produto(self, *produtos):
        for p in produtos:
            self.__produtos.append(p)

    def total(self):
        return sum([pro.preco for pro in self.__produtos])

    def path_produtos(self):
        print()
        cont = 1
        for p in self.__produtos:
            print("%d-%s \t %s" % (cont, p.nome, p.preco))
            cont+=1




class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


C1 = Carrinho()

refri1, refri2 = Produto("Coca-Cola 2L", 8.99), Produto("Dolly Guarana 2L", 3.22)

C1.append_produto(refri1, refri2)
print(C1.total())
C1.path_produtos()


print("\n")

# NOta a agragacao citada no texto, é um objeto que depende do outro
# ambos existem sozinhos, mas um precisa do outro para determinada acao metodo
# repare que os objetos (l.42) o carrinho precisa de outros objetos para determinar 
# seus metodos
# 


