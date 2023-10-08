dias = int(input("Quantos dias de dias de aluguel? "))
km = int(input("Quantos kmm rodados? "))
preco = (dias * 60) + (km * 0.15)
print(f"O total a pagar é {preco:.2f}")
