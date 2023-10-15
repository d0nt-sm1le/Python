n = float(input("Digite um número para ver a sua tabuada: "))
print("-=" * 10)
for x in range(0, 11):
    print(f"{int(n)} x {x} = {int(n * x)}")
print("-=" * 10)