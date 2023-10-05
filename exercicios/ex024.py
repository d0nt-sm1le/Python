x = list()
y = True

while y:
    x = int(input("Digite um valor: "))

    sn = str(input("Deseja continuar? "))
    if sn == 's':
        pass
    else:
        break
print(x)