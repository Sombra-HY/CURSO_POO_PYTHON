# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self._maodireita = None

    @property
    def maoDireita(self):
        return self._maodireita
    @maoDireita.setter
    def maoDireita(self, item):
        self._maodireita = item

    def personagem_segurando(self):
        return "o personagem pegou o(a) %s" % self.maoDireita

class Item:
    def __init__(self, nome):
        self.nome = nome

    def personagem_segurando(self):
        return "o personagem pegou o(a) %s" % self.nome

J1 = Personagem("Jose")

item1 = Item("Espada")
item2 = Item("Panela")

J1.maoDireita = item1

print(J1.__dict__)
print(J1.maoDireita.__dict__)

print("1 -", item1.personagem_segurando())
print("2 -", item2.personagem_segurando())
print("3 -", J1.maoDireita.personagem_segurando())
print(J1.maoDireita.nome)
print(J1.personagem_segurando())




















