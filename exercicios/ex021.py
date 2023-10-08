cidade = str(input("Qual o seu nome completo? ")).strip().upper()
if cidade.count("SILVA") == 1:
    print("O seu nome tem silva?", True)
else:
    print("O seu nome tem silva?", False)