# Mantendo estados dentro de classes

# E possivel alterar um atributo/Estado atraves de um metodo

# Exemplo: uma camera é inicializada com parametros marca/nome
# ao executar um metodo/ acao filmar ou tirar foto os parametros dele
# sao alterados (atributtos)

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print("%s, Já esta filmando!" % (self.nome))
        else:
            print("%s esta filmando..." % (self.nome))
            self.filmando = True
            # repare que o estado mudou, os valores padroes o
            # filmando passaram de false para true na segunda chamada do metodo

    def parar_filmar(self):
        if self.filmando:
            print("%s parou de filmar..." % (self.nome))
            self.filmando = False
        else:
            print("%s nao esta filmando!" % (self.nome))

    def fotografar(self):
        if self.filmando:
            print("Pare de filmar para tirar uma foto!")
        else:
            print("%s tirou uma foto!" % (self.nome))



c1 = Camera("Canon PRO 22K")
c2 = Camera("Sony HC2052")

c1.filmar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()
c1.fotografar()