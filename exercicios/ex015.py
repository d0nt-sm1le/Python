print("=" * 20)
print("Termos de P.A")
print("=" * 20)

z = int(input("Primeiro termo: "))
y = int(input("Razão: "))
tempo = z + (10 - 1) * y

for x in range(z, tempo + y, y):
    print(x, end=" -> ")

print("ACABOU")
