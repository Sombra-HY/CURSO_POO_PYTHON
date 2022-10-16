"""O try em conjunto com except serve como um formula para tratar possiveis erros, no caso
ele tenta um codigo, se ele retornar erro agora usara o except"""

x=input(": ")

try:
    print(x+1)
except:
    print(int(x)+1)