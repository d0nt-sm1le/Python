nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome...")
print(f"Seu nome em letras maiusculas é {nome.upper()}")
print(f"Seu nome em letras minusculas é {nome.lower()}")
print(f"Seu nome tem no total {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras")
