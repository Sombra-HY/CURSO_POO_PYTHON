from DADOS import produtos, nome, lista

valores = list(map(lambda x: "R$ %.2f"% x["valor"], produtos))
produto = list(map(lambda x: "%s, modelo %s custa "% (x["Produto"],x["Modelo"]), produtos))

print(*[x + y for x, y in zip(produto, valores)], sep="\n")


# MAP recebe uma funcao ou lambda e um valor ser iterado, tranforma em um iterador
# ex Map( lambda x :x * 2 , [1,2,3]) ---> cria um iterador 2, 4, 6
# basta trandormar em lista, caso necessario, list(map(...,...))