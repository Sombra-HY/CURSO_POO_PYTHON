z=input("Digite um numero inteiro positivo: ")
try:
    z=int(z)
    for x in range(z+1):
          print(x,z-x,sep="\t")
except:
    print("Digite apenas numeros inteiros positivos!")