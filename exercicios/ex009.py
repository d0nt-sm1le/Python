n = int(input("Digite um número para ver sua tabuada: "))

print("==" * 10)
for x in range(0, 11):
    print(f"{n} x {x} = {n * x}")
print("==" * 10)