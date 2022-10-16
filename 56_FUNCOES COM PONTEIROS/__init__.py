def soma(*aa,**luc):
    nome = luc.get("idade")
    print(nome)
soma(1,2,3,4,3,nome="lucas",sobrenome="jose")