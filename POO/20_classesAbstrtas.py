from abc import ABC,abstractmethod

class Log(ABC):

    @abstractmethod
    def _log(self):
        ...
    def log_sucess(self, msg):
        return self._log("sucess: (%s)"%msg)

    def log_error(self, msg):
        return self._log("error: (%s)"%msg)

class Print(Log):

    def _log(self, msg):
        print(self.__class__.__name__,msg)


l = Print()
l.log_sucess("deu ruim")
l.log_error("deu nada")