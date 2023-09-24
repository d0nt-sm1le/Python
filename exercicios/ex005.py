nt = float(input("Qual é a primeira nota do aluno? "))
nt2 = float(input("Qual é a segunda nota do aluno? "))
media = (nt + nt2) / 2

if media > 6.9:
    print(f"Tirando {nt} e {nt2}, a média do aluno é {media:.1f}")
    print("O aluno foi aprovado")
elif media >= 5.0:
    print(f"Tirando {nt} e {nt2}, a média do aluno é {media:.1f}")
    print("O aluno ficou recuperação")
elif media < 5.0:
    print(f"Tirando {nt} e {nt2}, a média do aluno é {media:.1f}")
    print("O aluno foi reprrovado")
else:
    print("Valor invalido , tente usar número quebrado como '7.8' e '5.0'")
