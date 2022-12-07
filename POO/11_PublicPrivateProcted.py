# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       so DEVE ser usado dentro da classe
#       ou em suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.


class Poo:
    # CONVECAO em java a o public protected e o private
    # no python a convencoes para os ambos que sao os usos do underline "_"

    def __init__(self):
        # Este public pode ser acessado no escopo todo do codigo ""
        # Este Protected so pode ser acessado dentro da classe e de suas subclasses "_"
        # Este Provate so pode ser usado na classe "__"
        self.public = "Valor Publico"
        self._protected = "Valor protegido"
        self.__private = "Valor privado"


    def metodo_publico(self):
        print("Esse metodo é publico, pois pode ser \nacessado pelo escopo todo do codigo!")

    def _metodo_protected (self):
        print("este metodo é protegido!!!")

    def __metodo_private(self):
        print("este metodo e privado!!!!!")


f = Poo()

# é possivel chamar os metodos e os atributos, mas nao deve ser feito

f.metodo_publico()
# print(f._Poo__metodo_private()) é possivel acessar mas nao e recomendado de maneira alguma



