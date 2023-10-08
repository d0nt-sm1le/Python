mf = input("Informe seu sexo [M/F]: ").strip().upper()

while mf != "F" and mf != "M":
    mf = input("Tente novamente: ").strip().upper()

if mf == "F":
    print("Registro FEMININO feito com sucesso!")
else:
    print("Registro MASCULINO feito com sucesso!")
