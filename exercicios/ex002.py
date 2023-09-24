n1 = int(input("Digite um valor: "))

print("Escolha uma das opções")
print("[ 1 ] Converter para BINÁRIO")
print("[ 2 ] Converter para OCTAL")
print("[ 3 ] Converter para HEXADECIMAL")
op = int(input("Sua opção: "))

if op == 1:
    bi = bin(n1)
    print(f"O número {n1} em binário é igual '{bi[2:]}'")
elif op == 2:
    oc = oct(n1)
    print(f"O número {n1} em octal é igual a '{oc[2:]}'")
elif op == 3:
    he = hex(n1)
    print(f"O número {n1} em hexadeciaml é igual a '{he[2:]}'")
else:
    print("Error 404 \nNot Found")
