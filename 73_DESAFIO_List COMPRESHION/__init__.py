carrinho = [("Camiseta 1", 35, 2), ("Camiseta 3", 56, 1), ("Camiseta 4", 89, 2), ("Camiseta 5", 4, 1)]

valor =sum([x[1] * x[2] for x in carrinho])

print(valor)