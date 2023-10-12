def terreno():
    la = float(input("Qual é a largura(m): "))
    c = float(input("Qual é o comprimento(m): "))
    re = la * c
    print(f"O comprimento da área é de {la}x{c} e sua área é de {re: .1f}m²")


print("Comprimento do terreno")
print("--" * 20)
terreno()
