co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipo = (co ** 2 + ca ** 2) ** (1/2)
print(f"O valor da hipotenusa é {hipo:.2f}")