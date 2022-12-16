# Abstracao

# LOG
# Heranca é um tipo 

# por exemplo o LogMixingFile é do tipo Log 
# O metodo _log é um intermediario do Log para as outras 
# classes que herdaram do Log. Assim como os metodos 

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

# O LOG é forma generica de tudo ( Assinatura da funcao )

class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o metodo LOG!")
    
    def log_error(self, msg):
        return self._log("Erro: %s" % msg)
    
    def log_sucess(self, msg):
        return self._log("Sucess: %s" % msg)


class LogMixxingFile(Log):
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__})'

        print(f"{msg_format}...")

        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_format+"\n")


class LogPrintMixxings(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ =='__main__':
    c = LogMixxingFile()
    c.log_sucess("Mensagem aleatoria do arquivo")
    c.log_error("sla o que escrever")
