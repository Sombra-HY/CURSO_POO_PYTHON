from DADOS import produtos, nome, lista

valores = list(map(lambda x: "R$ %.2f"% x["valor"], produtos))
produto = list(map(lambda x: "%s, modelo %s custa "% (x["Produto"],x["Modelo"]), produtos))

print(*[x + y for x, y in zip(produto, valores)], sep="\n")