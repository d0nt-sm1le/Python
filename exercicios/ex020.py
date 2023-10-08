cidade = str(input("Qual o nome da sua cidade? ")).strip().upper()
if cidade.count("SANTO") == 1:
    print(True)
else:
    print(False)