#criando CORDENADAS
def cord():
    l1 = [1, 2, 4, 8, 11, 30]
    l2 = [x * 2 for x in l1]

    cordenadas = [(x, y) for x in range(3) for y in l1]
    print(cordenadas)

# EMAILS CRIANDO

def email():
    nomes = ["lucas", "Maria", "Jose"]
    email = [name + "@gmail.com" for name in nomes]
    print(email)


#Invertendo valores de um tupla
def troca_chave():
    tupla = (
        ("chave1", "Valor1"),
        ("chave2", "Valor2"),
        ("chave3", "Valor3")
    )

    tupla_inv =[(z[1],z[0]) for z in tupla]
    print(dict(tupla_inv))
troca_chave()