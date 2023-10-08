valor = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(valor)}")
print(f"""Só tem espaços? {valor.isspace()}
É um número? {valor.isnumeric()}
É alfabético? {valor.isalpha()}
É alfanúmerico? {valor.isalnum()}
Está em maiúsculas? {valor.isupper()}
Está em minúsculas? {valor.islower()}
Está capitalizada? { valor.istitle()}""")
