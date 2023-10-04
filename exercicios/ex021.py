from random import randint

t1 = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9),)

print("O analfabeto funcional , os resultados foram esses aqui: ", end="")
for x in t1:
    print(x, end=" ")
print(f"\nO maior número sorteado foi {max(t1)}\nE o menor número sorteado foi {min(t1)}")
