string ="012345678901234567890123456789012345678901234567890123456789"
lista=[string[y-10:y].replace("9", "9.") for y in range(10,len(string)+10,10) ]
print("".join(lista))