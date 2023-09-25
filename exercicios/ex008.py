kg = float(input("Qual é o seu peso? (kg) "))
mm = float(input("Qual é a sua altura? (m) "))
imc = kg / (mm * mm)

if imc <= 18.5:
    print(f"O IMC dessa pessoa é igual {imc:.1f}")
    print(f"Você está ABAIXO DO PESO NORMAL!")

elif imc <= 25:
    print(f"O IMC dessa pessoa é igual {imc:.1f}")
    print(f"PARABENS! Você está no peso ideal")

elif imc <= 30:
    print(f"O IMC dessa pessoa é igual {imc:.1f}")
    print(f"Você está com SOBREPESO")

elif imc <= 40:
    print(f"O IMC dessa pessoa é igual {imc:.1f}")
    print(f"Você está em OBESIDADE")

else:
    print(f"O IMC dessa pessoa é igual {imc:.1f}")
    print(f"Você está em OBESIDADE MÓRBIDA, cuidado!")
