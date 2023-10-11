def terrenos():
    print("Comprimento do terreno")
    print("--" * 10)

    largura = float(input("Digite a altura(m): "))
    comprimento = float(input("Digite a largura(m): "))
    com = largura * comprimento

    print(f"A área do perimetro é de {largura}x{comprimento} e sua área é de {com:.1f}m²")


terrenos()

