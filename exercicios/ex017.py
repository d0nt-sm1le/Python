def txt(x):
    print(x)


nome = str(input("Digite seu nome completo: ")).strip()
print("analisando o seu nome...")
txt(f"Seu nome em maiúsculas é {nome.upper()}")
txt(f"Seu nome em minusculas é {nome.lower()}")
txt(f"Seu nome ao todo tem {len(nome) - nome.count(" ")}")
txt(f"Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras")