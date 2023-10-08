from random import randint

numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),)

print("Os números digitados foram:", numeros[0], numeros[1], numeros[2], numeros[3])
print(f"O maior valor digitado foi: {max(numeros)}\nO menor valor digitado foi: {min(numeros)}")
