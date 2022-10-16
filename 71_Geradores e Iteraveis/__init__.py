import sys
import time

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13]
lista1 = [x for x in range(0,100000)]
lista2 = (1,2,3,4,6,7,8,9,0)
lista3 = (x for x in range(0,100000))
print(sys.getsizeof(lista),"Bytes")
print(sys.getsizeof(lista1),"Bytes")
print(sys.getsizeof(lista2),"Bytes")
print(sys.getsizeof(lista3),"Bytes")

def valor():
    for x in range(100):
        time.sleep(1)
        print(".",end="")

print(valor())