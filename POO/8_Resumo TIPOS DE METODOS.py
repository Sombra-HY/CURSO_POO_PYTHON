# Metodo vs Classe do Metodo vs Metodo Estatico
#   self vs          cls     vs  none
#           @classmethod         @staticmethod



class Conection:

    # Utilizacao do self é metodo de instancia
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    # Metodo de classe
    @classmethod
    def auth(cls, user, password):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection

    @staticmethod
    def log(msg):
        print("\nLOG: %s"%(msg))

    def path_acount(self):
        print("Informacoes da conta\n\nUsuario: %s\nSenha: %d"%(self.user, self.password))


c2 = Conection.auth("lucas", 123465)
c2.path_acount()
Conection.log("erro faltal!")
