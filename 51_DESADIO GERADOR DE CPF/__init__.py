from random import randint

cpf = str(randint(100000000, 999999999))
for y in range(2):
    soma=0
    for x, z in zip(range(1-y, len(cpf)+y+1), cpf):
        soma += int(z) * x
    cpf = cpf + "0" if soma % 11 >= 10 else cpf + str(soma % 11)
cpf_c = cpf[0:3] +"." + cpf[3:6] +"."+ cpf[6:9]+"-"+cpf[9:]
