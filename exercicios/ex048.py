pessoas = list()
dados = list()
contagem = 0

while True:
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite seu peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    s = str(input("Deseja continuar?[S/N] ")).strip().lower()
    if s == 'n':
        break
    else:

        pass
po = pessoas.index(max(pessoas))
pe = pessoas.index(min(pessoas))
print(f"Ao todo você cadatrou {len(pessoas[:][0])} pessoas")
print(f"O maior peso foi de {max(pessoas[0:][0:])[1]}kg.",end="")

if max(pessoas) in pessoas[:]:
    print(f"Que é de {pessoas[po][0]}")

print(f"O maior peso foi de {min(pessoas[0:][0:])[1]}kg.",end="")

if max(pessoas) in pessoas[:]:
    print(f"Que é de {pessoas[pe][0]}")