def aux(*args):
    return sum(args)
#somar as variaveis

def metre(funcao, *args):
    valor=funcao(*args)
    return str(valor) + " corno(s)"



valor = metre(aux,1,2,3)

print(valor)