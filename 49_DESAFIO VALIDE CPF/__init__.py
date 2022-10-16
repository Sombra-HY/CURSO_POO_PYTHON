def vald_cpf(cpf=input("Digite seu CPF: ")):
    try:
        #TRATAMENTO DE DADOS
        for carcter in [".", ",", "-", ";", " "]:
            cpf = cpf.replace(carcter, "")
            # condicao de erro
            erro = 9/0 if (len(cpf)!=11 and cpf.isdigit()) else 0
        #VALIDACAO DE DADOS
        for z in range(2):
            soma = 0
            for num, x in zip(cpf, range(1,10+z)):
                soma += int(num) * (x-z)
            vef = 0 if soma % 11>=10 else soma % 11
            if vef !=int(cpf[9+z]):
                print("O CPF invalido! ")
                break
    except ZeroDivisionError:
        print("Digite 11 numeros para o CPF!")
    except:
        print("O CPF nao tem letras!")
    else:
        print("O CPF e valido!")
vald_cpf()