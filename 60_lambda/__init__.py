
lista = [["P4",8], ["P2",2], ["P3",4]]

def fuc(iten):
    return iten[0]



#lista.sort(key=fuc)

lista.sort(key = lambda item:item[0])


print(lista)


