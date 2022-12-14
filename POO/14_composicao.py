# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append( Endereco(rua, numero))

    def mostrar_enderecos(self):
        for clientes in self.endereco:
            print(clientes.rua, clientes.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua 
        self.numero= numero 

e1 = Cliente("lucas")
e1.inserir_endereco("Rua ticol silva", 34)
e1.inserir_endereco("Rua jose de alencar", 56)
e1.mostrar_enderecos()  

# Existe um dependencia da class endereco ao cliente
# ou seja se o cliente for apagado o endereco tambem vai ser...