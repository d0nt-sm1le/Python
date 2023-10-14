def variaveis(x):
    print(x)


algo = input("Digite algo: ")
variaveis(f"O tipo primitivo desse valor é {type(algo)} ")
variaveis(f"É um número? {algo.isnumeric()}")
variaveis(f"É alfabético? {algo.isalpha()}")
variaveis(f"É alfanúmerico? {algo.isalnum()}")
variaveis(f"Está em maiúsculas? {algo.isupper()}")
variaveis(f"Está em minusculas? {algo.islower()}")
variaveis(f"Está capitalizada? {algo.istitle()}")
