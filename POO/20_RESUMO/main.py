
# HERANCA MUTIPLA 

from eletronico import Smartphone


galaxy = Smartphone("Galaxy A11")
iphone = Smartphone("Iphone 12")

galaxy.desligar()
iphone.ligar()
#           DIAGRAMA DE HERANCAS
#
#                     (LOG)                                  ELETRONICO
#                    /     \                                   /
#       LogMixxingFile     LogPrintMixxings                   / 
#              \                /                            /
#               \      OU      /                            / 
#                \            /                            /
#                 \          /          heranca principal / 
#                  Smartphone ___________________________/
# Na duvida, nao use heranca, vai ficando cada vez pior