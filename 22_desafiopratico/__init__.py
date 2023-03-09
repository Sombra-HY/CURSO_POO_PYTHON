perguntas = ["Qual e o seu nome? "," Qual seu ano de nascimento: ","Qual e o seu peso? (Kg) ", " Qual e a sua altura?"]
resposta = []

for x in range(len(perguntas)):

    if x==0:
        resposta.append(input("%s\n" % perguntas[x]))

    elif x!=0:

        resposta.append(float(input("%s\n" % perguntas[x])))

print("\n%s tem %d anos, pesa %.2f kg e tem %.2f metros de altura.\n"% 
(resposta[0], 2022-int(resposta[1]),resposta[2],resposta[3]),
      "O IMC de %s e %.2f.\n"% (resposta[0], 10),
      "%s nasceu em %s.\n"% (resposta[0], resposta[1]),sep="")


print