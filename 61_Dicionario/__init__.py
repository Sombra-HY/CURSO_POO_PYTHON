Dados = {
    "001":{
        "Nome":"Lucas",
        "Sobrenome":"Sombra",
        "Idade":19,
        "Sexo":"M"
    },
    "002":{
        "Nome":"Jose",
        "Sobrenome":"da Silva",
        "Idade":34,
        "Sexo":"M"
    },
    "003":{
        "Nome":"Maria",
        "Sobrenome":"Sonia Oliveira",
        "Idade":20,
        "Sexo":"F"
    }
}


for id,  cliente in Dados.items():
    print("\n\n{}:".format(id))

    for dados in cliente:
        if dados == "Idade":
            print("\n%d anos\n"%cliente[dados])
            continue
        if dados == "Sexo":
            print("%s\n"%cliente[dados])
            continue
        print("{}".format(cliente[dados]) ,end=" ")
