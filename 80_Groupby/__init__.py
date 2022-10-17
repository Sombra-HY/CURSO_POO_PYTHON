from itertools import groupby,tee

carros = [
    {"Modelo": "Ferari zika", "ano": 2010},
    {"Modelo": "Celta", "ano": 2003},
    {"Modelo": "Civic", "ano": 2022},
    {"Modelo": "Ferrari", "ano": 2006},
    {"Modelo": "HB20", "ano": 2010},
]

# escolho como dever a orden
orden = lambda x: x["ano"]

# coloca os valores do dicionario na orden que desejo no caso a "orden"
carros.sort(key=orden)

a = groupby(carros, orden)
for x in a:
    ger = tee(x[1],2)                                                                 # [(2020,{items}),(2022,{items}),(2003,{items})]
    print("\n", x[0]," Existem %d elemento(s)"%(
        len([x for x in ger[0]])
    ), sep="")
    for y in ger[1]:                                                                          # ({items}) ({items}) ({items})
        print(y["Modelo"])