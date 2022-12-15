# super() e a sobreposição de membros - Python Orientado a Objetos
# o super acessa um metodo dentro deste... super(self,C) == super()
# os parametros sao colocados por padrao
# ao chama or super ele comeca a ver por quem foi enviado, por exemplo
# a sobreposciao esta assim [A,B,C] ao passar super(B, self) estando no C
# ele irra para o A, o posterior...
# print(C.mro()) <-- Method Resolution Order

# CONJUTO -->   (C (B (A ) ) )


class A:
    atributo_a = "a"
    def metodo(self):
        print("sou A!")

class B(A):
    atributo_b = "b"
    def metodo(self):
        print("sou B!")


class C(B):
    atributo_c = "c"

    def metodo(self):
        super( B, self).metodo() # nao e necessario colocar parametros no super...
        print("sou C!")

conjunto = C()

# O B herdou o A e o C herdou o B, portanto o C herdou tanto B quanto o A   

print(conjunto.atributo_a)
print(conjunto.atributo_b)
print(conjunto.atributo_c)
conjunto.metodo() 

print(C.mro())
# por causa da Method resolution order: help(C) <-- execultar pra ver o que eesta acontecendo 

# para acessar um metodo que foi sobreposto é preciso usar o super()