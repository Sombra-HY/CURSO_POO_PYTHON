" Operador ternario e uma expressao de vdd ou falso dento do var"

idade = input("Digite sua idade: ")
try:
    msg = "Maior de Idade" if int(idade)>=18 else "Menor de Idade"
except:
    msg = "Digite apenas numeros!"
print(msg)