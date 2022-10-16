
def saudacao(name,sadau):
    print(sadau,name+"!",sep=", ")
def porce(valor,porc):
    return valor*(1+porc)
def som(x,y,z):
    return x+y+z
def buzz(x):
    return \
        "FizzBuzz" if (x%5==0 and x%3==0) else "Buzz" \
        if (x%5==0) else "Fizz" \
        if (x%2==0) else "%d"%x

saudacao("Lucas Sombra", "Bem vindo")
print(porce(355,0.10))
print(som(2,3,5))
print(buzz(11))
