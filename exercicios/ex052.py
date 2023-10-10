pessoas = dict()
np = list()
idade = list()

while True:
    pessoas['nome'] = input("Nome: ").capitalize().strip()
    pessoas['sexo'] = str(input("Digite seu sexo:[M/F] ")).lower().strip()

    if pessoas['sexo'] != 'm' or pessoas['sexo'] != f':
        while True:
            pessoas['sexo'] = str(input("Parece que não deu certo, tente novamente:[M/F] ")).lower().strip()
            if pessoas['sexo'] == 'm' or pessoas['sexo'] == 'f':
                break

    pessoas['idade'] = int(input("Digite sua idade: "))
    if pessoas['idade'] > 110 or pessoas['idade'] < 0 or pessoas['idade'] != int:
        while True:
            pessoas['idade'] = int(input("Parece que não deu certo, tente novamente: "))
            if pessoas['idade'] < pessoas['idade'] > 0 or pessoas['idade'] == int:
                break
            else:
                pass
